import tweepy

from authentication.Basic_auth import auth


api=auth()

# This example will download your home timeline tweets and print each one of their texts to the console.

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text