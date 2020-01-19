import tweepy
from textblob import TextBlob
import config

auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

tweets = api.search('Austria')

for tweet in tweets :
    analysis = TextBlob(tweet.text)
    if analysis.polarity > 0.25 :
        print('\n')
        print(tweet.text)
        print(analysis.sentiment)
        print('Polarity:', analysis.polarity)
