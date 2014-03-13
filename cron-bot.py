import csv
import time
import datetime
import tweepy

# cron settings
# * * 12 03 * python /home/denten/gDrive/Code/Litclock/cron-bot.py
# paths have to be explicit for cron
path = '/home/denten/gDrive/Code/Litclock/'


# separate the credits out to keep out of github
def getcreds():
    with open(path + 'creds.csv', 'r') as csvfile:
        creds = csv.DictReader(csvfile, delimiter=",")

        row = creds.next()

        return row['token'], row['secret'], row['akey'], row['asecret']


# get the text corresponding to current time
def gettext():

    now = datetime.datetime.now().time()

    with open(path + 'tweets.csv', 'r') as csvfile:
        tweets = csv.DictReader(csvfile, delimiter=",")

        for row in tweets:

            ft = row['time']
            hour = int(ft.split(':')[0])
            minute = int(ft.split(':')[1])

            if hour == now.hour and minute == now.minute:
                return row['text']


# tweet
def tweet(k, t):

    try:
        # k stores token, secret, api key, and api secret
        auth = tweepy.OAuthHandler(k[2], k[4])
        auth.set_access_token(k[0], k[1])

        api = tweepy.API(auth)
        api.update_status('test')

        # dummy write to a file instead of tweeting
        # f = open(path + 'log.txt', 'a')
        # f.write(t + '\n')
    except:
        pass

# get creds > get text > tweet
keys = getcreds()
text = gettext()
tweet(keys, text)
