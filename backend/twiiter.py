import twint
import os
import json
import uuid
from config import tweetpath
from deep_translator import GoogleTranslator
import pandas as pd
import time


def top_tweets(username):
    for user in username:
        c = twint.Config()
        c.Limit = 20
        path = os.path.join(
            tweetpath, f"NDRF_tweets_{str(uuid.uuid4())}_.json")
        c.Output = path
        c.Store_json = True
        c.Username = user
        c.Filter_retweets = True
        a = twint.run.Search(c)

    # scrapping done & preprocessing start
    totalTweets = {}
    for user in username:
        tweets = []
        for line in open(path, 'r', encoding="utf8"):
            tweets.append(json.loads(line))
            totalTweets[user] = tweets

    data = json.dumps(totalTweets[user])
    data_sorted = pd.read_json(data)
    data_sorted = data_sorted.drop(['mentions', 'created_at', 'date', 'user_rt_id', 'user_rt', 'retweet_id', 'reply_to', 'retweet_date', 'trans_src',
                                    'trans_dest', 'cashtags', 'retweet', 'quote_url', 'place', 'conversation_id', 'id'], axis=1)
    #data_sorted['translated'] = data_sorted.apply(lambda x: g_translation_function_en(data_sorted['tweet']))
    print('\nTwitter data scrapped !\n')

    data_return = data_sorted.to_json(orient='records')

    userinfo = json.loads(data_return)[0]
    print(data_return)
    temp = userinfo['tweet']
    userinfo['tweet'] = []
    userinfo['tweet'].append(temp)
    data_return2 = json.loads(data_return)
    for tweet in data_return2:
        userinfo['tweet'].append(tweet['tweet'])

    return userinfo, json.loads(data_return)


def g_translation_function_en(inText):
    try:
        if len(inText) <= 4999:
            outText = GoogleTranslator(
                source='auto', target='en').translate(inText)
            return outText
        else:
            return inText
    except Exception as e:
        print(e)
        return inText
