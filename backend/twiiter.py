import twint
import os
import json
import uuid
from config import tweetpath
import pandas as pd


def top_tweets(username):
    for user in username:
        c = twint.Config()
        c.Limit = 2
        c.Min_likes = 1
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
        for line in open(path, 'r'):
            tweets.append(json.loads(line))
            totalTweets[user] = tweets

    data = json.dumps(totalTweets[user])
    data_sorted = pd.read_json(data)
    data_sorted = data_sorted.drop(['mentions','created_at','date', 'user_rt_id', 'user_rt', 'retweet_id', 'reply_to', 'retweet_date', 'trans_src',
                     'trans_dest', 'cashtags', 'retweet', 'quote_url', 'place', 'conversation_id', 'id'], axis=1)
    print('\nTwitter data scrapped !\n')
    return data_sorted.to_dict()
