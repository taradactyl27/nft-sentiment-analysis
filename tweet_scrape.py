import tweepy
import time

# create file twitter_credentials.py with these credential fields from the twitter API
from twitter_credentials import consumer_key, consumer_secret, access_token, access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

positive_projects = [
    "Bored Ape Yacht Club",
    "Cool Cat Club",
    "Gutter Cat Gang"
]
negative_projects = [
]

for i in range(20):
    print("Getting data. Iteration",i+1)
    for proj in positive_projects + negative_projects:
        text = ""
        # get this to run every x min
        public_tweets = api.search_tweets(proj)
        for tweet in public_tweets:
            text += tweet.text + " "

        with open("./data/" + proj.replace(" ","_") + "_text.txt", "a") as f:
            f.write(text)

    time.sleep(60*5)
