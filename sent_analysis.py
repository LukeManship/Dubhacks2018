# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 23:43:59 2018

@author: Nick
"""

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob
import twitterscraper

class TwitterClient(object):
    
    def __init__(self):
        """
        Establishes keys and tokens from twitter dev console, attempts
        authentication to app
        """
        consumer_key = 'vgvd3ANm4sydRn5NV2nMYRyO5'
        consumer_secret = 'yRtS9MCId0wyH6qQJ8Bnq7eF1n0CrqC9NCwLZAxjy2UKzpJy3i'
        access_token = '1053780358091571200-dPY22sLhFKjGu9JLiw4O5HG954cvQR'
        access_token_secret = 'dc5jRxBwswTE0G3cgtDnHeC5F7QaNiwx3V9WCSus9eQOg'
        
        try:
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            self.auth.set_access_token(access_token, access_token_secret)
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")
        
    def clean_tweet(self, tweet):
        """
        Cleans tweet text, removing links, special characters
        """
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t]) | (\w+:\/\/\S+)", " ", tweet).split()) 
        
    def get_sentiment(self, tweet):
        analysis = TextBlob(self.clean_tweet(tweet))
        
        pol = analysis.sentiment.polarity
        
        if pol > 0:
            return 'positive'
        elif pol == 0:
            return 'neutral'
        else:
            return 'negative'
        
    