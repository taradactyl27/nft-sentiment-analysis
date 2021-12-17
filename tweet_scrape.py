import tweepy
import time
import json
import sys
import pandas as pd

from tweepy import Stream

# create file twitter_credentials.py with these credential fields from the twitter API
from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

genuine_proj = ["cool cats nft", "world of women nft", "robotos nft", "doodles nft"]
scam_proj = ["angry anglers", "baller ape club"]

for proj in genuine_proj + scam_proj:
    filename = "_".join(proj.split(" ")) + ".csv"
    print("Collecting tweets for:", proj)
    print("Writing results to", filename)

    resp = api.search_full_archive("prod", proj)

    tweets = []
    timestamps = []

    for status in resp:
        tweets.append(status.text)
        timestamps.append(status.created_at)

    df = pd.DataFrame({
            "tweets": pd.Series(tweets),
            "timestamps": pd.Series(timestamps)
            })

    df.to_csv(filename)
