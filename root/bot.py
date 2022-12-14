import os
import tweepy

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("api_key")
API_SECRET = os.environ.get("api_key_secret")
API_TOKEN = os.environ.get("bearer_token")
ACCESS_TOKEN = os.environ.get("access_token")
ACCESS_TOKEN_SECRET = os.environ.get("access_token_secret")


auth = tweepy.OAuth1UserHandler(
   API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
)

api = tweepy.API(auth)
api.update_status("Test tweet")
