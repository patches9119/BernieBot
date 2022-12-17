import os
import time
import tweepy
import textwrap

from dotenv import load_dotenv
load_dotenv()

# opens and reads the text file full of aggregated pregenerated tweets and puts it into an array
file = open('root/tweets.txt', 'r')
read = file.read().split('====================')
modified = [] ##for use later

# double checks for duplicates and removes line breaks and moves it into a new array
for line in read:
   if line not in modified:
      modified.append(line.strip())
# print(modified)


# all sensitive information is stored using enviormental variables
API_KEY = os.environ.get("api_key")
API_SECRET = os.environ.get("api_key_secret")
API_TOKEN = os.environ.get("bearer_token")
ACCESS_TOKEN = os.environ.get("access_token")
ACCESS_TOKEN_SECRET = os.environ.get("access_token_secret")


# required setup for tweepy to funtion
auth = tweepy.OAuth1UserHandler(
   API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)
api = tweepy.API(auth)
client = tweepy.Client(API_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


# gets the latest tweet from the bot that was posted
def getLastTweet():
   tweets_list = api.user_timeline()
   return tweets_list[0].id

# used to split longer generations up and tweet them sperately
# tweets after the first will be sent as replies to avoid any confusion on the timeline
def sendMultiTweet(tweet):
   tweets = textwrap.wrap(tweet, 280)
   api.update_status(tweets[0])
   # print(tweets[0])
   tweets.pop(0)
   for tweet in tweets:
      lastTweet = getLastTweet()
      # print(tweet)
      # print("Last tweet: ",lastTweet)
      api.update_status(status = tweet, in_reply_to_status_id = lastTweet , auto_populate_reply_metadata=True)
   # print("successfully Tweeted!")

# main function that will have the bot tweet out once every 6 hours until it runs out of tweets
#
# this functionality would be fixed in a later update not either not using hand chosen tweets in a text file or...
# ...moving the tweet storage to another system that can be changed on the fly such as a google sheet
def botMain():
   for tweet in modified:
      if(len(tweet) < 280):
         api.update_status(tweet)
         # print("Tweeted successfully!")
      else:
         sendMultiTweet(tweet)
   time.sleep(21600)

botMain()