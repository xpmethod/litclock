import csv
import time
import datetime
from apscheduler.scheduler import Scheduler

# Using threading for now to schedule, but probably safer to run
# a cron job

def tweetbot():
    # open takes the name of the file and modes like read and write
    with open('tweets.csv', 'r') as csvfile:
        tweetreader = csv.DictReader(csvfile, delimiter=",")

        for row in tweetreader:
            ft = row['time']
            hour = int(ft.split(':')[0])
            minute = int(ft.split(':')[1])
            now = datetime.datetime.now().time()
            if hour == now.hour and minute == now.minute:
                print row['text']

    threading.Timer(60, tweetbot).start()

tweetbot()
