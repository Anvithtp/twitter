Nithin Naik10:29 AM
import tweepy
import os

consumer_key = os.getenv('consumer_key)
consumer_secret = os.getenv('consumer_secret)
access_token = os.getenv('access_token)
access_token_secret = os.getenv('access_token_secret)

auth =tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

import time
while True:
  user = api.get_user('anvith_tp')
  n = user.followers_count
  api.update_profile(name =f'anvith tp {n} followers ')
print(f'ANVITH TP {n} Followers)
  time.sleep(60)
          
           
  
