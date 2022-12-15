import os
import time
import tweepy
import textwrap

from dotenv import load_dotenv
load_dotenv()

file = open('root/tweets.txt', 'r')
read = file.read().split('====================')
modified = []

for line in read:
   if line not in modified:
      modified.append(line.strip())
# print(modified)

API_KEY = os.environ.get("api_key")
API_SECRET = os.environ.get("api_key_secret")
API_TOKEN = os.environ.get("bearer_token")
ACCESS_TOKEN = os.environ.get("access_token")
ACCESS_TOKEN_SECRET = os.environ.get("access_token_secret")


auth = tweepy.OAuth1UserHandler(
   API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)
client = tweepy.Client(API_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

def getLastTweet():
   tweets_list = api.user_timeline()
   return tweets_list[0].id

def sendMultiTweet(tweet):
   tweets = textwrap.wrap(tweet, 280)
   api.update_status(tweets[0])
   print(tweets[0])
   tweets.pop(0)
   for tweet in tweets:
      lastTweet = getLastTweet()
      print(tweet)
      print("Last tweet: ",lastTweet)
      api.update_status(status = tweet, in_reply_to_status_id = lastTweet , auto_populate_reply_metadata=True)
   print("successfully Tweeted!")

for tweet in modified:
   if(len(tweet) < 280):
      api.update_status(tweet)
      print("Tweeted successfully!")
   else:
      sendMultiTweet(tweet)
   time.sleep(120)