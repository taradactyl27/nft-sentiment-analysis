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

filename = "_".join(sys.argv[1].split(" ")) + ".csv"
print("Collecting tweets for:", sys.argv[1])
print("Writing results to", filename)

try:
    df = pd.read_csv("./data/{}".format(filename))
    tweets = df["tweets"]
    timestamps = df["timestamps"]

except Exception:
    tweets = pd.Series()
    timestamps = pd.Series()
    
class Listener(Stream):
    def on_data(self,data):
        try:
            resp = json.loads(data.decode('utf8'))

            tweets = tweets.append(pd.Series(resp["text"]))
            timestamps = timestamps.append(pd.Series(resp["created_at"]))

            self.count += 1
            print("collected",self.count,"tweets")

            if self.count % 10 == 0:
                df = pd.DataFrame([tweets, timestamps], columns=["tweets","timestamps"])
                df.to_csv(filename)

        except Exception as e:
            print(e)

        return True

    def on_request_error(self,status):
        print(status)

stream = Listener(consumer_key, consumer_secret, access_token, access_token_secret)
stream.count = 0
stream.filter(track=[sys.argv[1]])
