import csv
import time
import datetime
import pdb

# open takes the name of the file and modes like read and write
with open('tweets.csv', 'r') as csvfile:
    tweetreader = csv.DictReader(csvfile, delimiter=",")
    for row in tweetreader:
        ft = row['time']
        hour = ft.split(':')[0]
        minute = ft.split(':')[1]
        now = datetime.datetime.now().time()
        if hour == now.hour and minute == now.minute:
            pdb.set_trace()
            print row['text']
