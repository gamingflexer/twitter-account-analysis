from model import predict_text_class
import pandas as pd
import json

def rank_text(text):
    return predict_text_class(text,MAX_LEN=64)


def pie_chart_rank(data):
    rank_list = []
    for i in data:
        rank = rank_text(i['tweet'])
        rank_list.append(rank)
        
    for i in rank_list:
        for key,value in i.items():
            value = value * 100
            i[key] = value
    
    df = pd.read_json(json.dumps(rank_list))
    df2 = df.sum(axis=0)
    data_dict = df2.to_dict()
    data_pie = {}
    data_pie['labels'] = list(data_dict.keys())
    data_pie['data'] = list(data_dict.values())

    return data_pie

#print(pie_chart_rank([{'tweet':"First and last warning, you fucking gay - I won't appreciate if any more nazi shwain would write in my page! I don't wish to talk to you anymore! Beware of the Dark Side!"},{'tweet':"Tony Sidaway is obviously a fistfuckee. He loves an arm up his ass"}])) 