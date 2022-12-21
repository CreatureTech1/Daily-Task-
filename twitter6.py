import tweepy
 
import pandas as pd
import csv
import re 
import string
import preprocessor as p
 
consumer_key = "b8H0AinqH3wGbVkmpKsldJfKz"
consumer_secret = "5Wyj0ay8Elo5gXdidY6sXcC6ByDrHilVnnXWtY4wWNRJeRhqPS"
access_key= "1295683057-gfcfWdaP3bEp87hus8oMg5GaZDUtTuxM8vCjFF9"
access_secret = "yylD20FDA2FloPwoc2WOTh4L2iUSuwUfCJsZ451URB2DB"
 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
 
api = tweepy.API(auth,wait_on_rate_limit=True)
 
csvFile = open('file-name', 'a')
csvWriter = csv.writer(csvFile)
 
search_words = "Arun"      # enter your words
new_search = search_words + " -filter:retweets"
 
for tweet in tweepy.Cursor(api.search_tweets,q=new_search,count=100,
                           lang="en",
                           since_id=0).items():
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.user.screen_name.encode('utf-8'), tweet.user.location.encode('utf-8')])
