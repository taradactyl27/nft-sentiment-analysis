import tweepy
import time
import json
import sys

from tweepy import Stream

# create file twitter_credentials.py with these credential fields from the twitter API
from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

filename = "_".join(sys.argv[1].split(" "))
print("Collecting tweets for:", sys.argv[1])
print("Writing results to", filename)

class Listener(Stream):
    def on_data(self,data):
        try:
            text = json.loads(data.decode('utf8'))['text']
            with open("./data/{}.txt".format(filename),"a") as f:
                f.write(text)

            self.count += 1
            print("collected",self.count,"tweets")

        except Exception as e:
            print(e)

        return True

    def on_request_error(self,status):
        print(status)

stream = Listener(consumer_key, consumer_secret, access_token, access_token_secret)
stream.count = 0
stream.filter(track=[sys.argv[1]])
