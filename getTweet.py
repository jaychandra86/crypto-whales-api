import re
import config
import tweepy
import requests
import time

import getWhale


def loginToTwitter():
    try:
        print("Logging into Twitter")
        auth = tweepy.OAuthHandler(config.consumer_key, config.consumer_secret)
        auth.set_access_token(config.access_token, config.access_token_secret)
        api = tweepy.API(auth)
    except Exception as e:
        print("Something went wrong while logging into twitter.")
        print(e)

    return api

def getTweet(api):
    try:
        print("-----------------------------------------------")
        userID = "whale_alert"

        res = []
        emojis_to_remove = ['💵', '🔥', '🚨']

        tweetCount = 15

        tweets = api.user_timeline(screen_name=userID,
                           # 200 is the maximum allowed count
                           count=tweetCount,
                           include_rts = False,
                           # Necessary to keep full_text
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended'
                           )

        for info in tweets[:tweetCount]:
            #extract the tweet

            tweet = (info.full_text)

            tweet = ("".join(ch for ch in tweet if ch not in emojis_to_remove)).lstrip()

            #print(tweet)
            #replace new line characters
            tweet = tweet.replace("\n", " ")

            #get the t.co url
            tcoUrl = re.findall(r'(https?://\S+)', tweet)[-1]

            #remove t.co url from the tweet
            tweet = tweet.replace(tcoUrl, "")

            tweet = re.sub('[^A-Za-z0-9]+', ' ', tweet)
            #get the original url from t.co url
            r = requests.get(tcoUrl)
            url = r.url

            #get the transaction data from whale-alert.io
            data = getWhale.getData(url)
            #time.sleep(10)
            #data = "hello"
            #append it to result
            res.append(data)
            time.sleep(10)


    except Exception as e:
        print('* Something went wrong while getting tweet')
        print("-----------------------------------------------")
        print(e)

    return res


"""api = loginToTwitter()

t = getTweet(api)

print(t)
"""
