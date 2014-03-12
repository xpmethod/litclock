import csv
import time
import datetime

# cron settings
# * * 12 03 * python /home/denten/gDrive/Code/Litclock/cron-bot.py
# paths have to be explicit for cron

path = '/home/denten/gDrive/Code/Litclock/'

with open(path + 'tweets.csv', 'r') as csvfile:
    tweetreader = csv.DictReader(csvfile, delimiter=",")

    for row in tweetreader:
        ft = row['time']
        hour = int(ft.split(':')[0])
        minute = int(ft.split(':')[1])
        now = datetime.datetime.now().time()
        if hour == now.hour and minute == now.minute:
            # print row['text']
            f = open(path + 'log.txt', 'a')
            f.write(row['text'] + '\n')
