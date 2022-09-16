import os
import numpy as np
import pandas as pd
import tensorflow as tf
from transformers import TFBertModel
from transformers import BertTokenizer
from tensorflow.keras.layers import Dense, Flatten
from keras_preprocessing.sequence import pad_sequences

from constants import label_cols

class BertClassifier(tf.keras.Model):    
    def __init__(self, bert: TFBertModel, num_classes: int):
        super().__init__()
        self.bert = bert
        self.classifier = Dense(num_classes, activation='sigmoid')
        
    @tf.function
    def call(self, input_ids, attention_mask=None, token_type_ids=None, position_ids=None, head_mask=None):
        outputs = self.bert(input_ids,
                               attention_mask=attention_mask,
                               token_type_ids=token_type_ids,
                               position_ids=position_ids,
                               head_mask=head_mask)
        cls_output = outputs[1]
        cls_output = self.classifier(cls_output)
                
        return cls_output

MODEL_PATH_BERT2 = './model/bert_toxic_2/'

MODEL_BERT2 = BertClassifier(TFBertModel.from_pretrained('bert-base-uncased'), len(label_cols))
MODEL_BERT2.load_weights(MODEL_PATH_BERT2)
tokenizer_BERT2 = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)

print("\BERT MULTI MODEL LOADDED\n")

def tokenize_sentences_multiclass(sentences, tokenizer, max_seq_len = 128):
    tokenized_sentences = []

    for sentence in sentences:
        tokenized_sentence = tokenizer.encode(
                            sentence,                  # Sentence to encode.
                            add_special_tokens = True, # Add '[CLS]' and '[SEP]'
                            max_length = max_seq_len,  # Truncate all sentences.
                    )
        
        tokenized_sentences.append(tokenized_sentence)

    return tokenized_sentences


def create_dataset_multiclass(data_tuple, epochs=1, batch_size=32, buffer_size=10000, train=True):
    dataset = tf.data.Dataset.from_tensor_slices(data_tuple)
    if train:
        dataset = dataset.shuffle(buffer_size=buffer_size)
    dataset = dataset.repeat(epochs)
    dataset = dataset.batch(batch_size)
    if train:
        dataset = dataset.prefetch(1)
    
    return dataset

def create_attention_masks(tokenized_and_padded_sentences):
    attention_masks = []

    for sentence in tokenized_and_padded_sentences:
        att_mask = [int(token_id > 0) for token_id in sentence]
        attention_masks.append(att_mask)

    return np.asarray(attention_masks)

def predict_text_class(text,MAX_LEN=64):
  test_input_ids = tokenize_sentences_multiclass(text, tokenizer_BERT2, MAX_LEN)
  test_input_ids = pad_sequences(test_input_ids, maxlen=MAX_LEN, dtype="long", value=0, truncating="post", padding="post")
  test_attention_masks = create_attention_masks(test_input_ids)
  test_dataset = create_dataset_multiclass((test_input_ids, test_attention_masks), batch_size=1, train=False, epochs=1)
  for i, (token_ids, masks) in enumerate(test_dataset):
    #sample_ids = df_test.iloc[i*TEST_BATCH_SIZE:(i+1)*TEST_BATCH_SIZE]['id']
    predictions = MODEL_BERT2(token_ids, attention_mask=masks).numpy()
    return predictions[0]