import csv
import time
import datetime
from apscheduler.scheduler import Scheduler

sched = Scheduler()
@sched.interval_schedule(seconds=60)
def twitterbot():
    with open('tweets.csv', 'r') as csvfile:
        tweetreader = csv.DictReader(csvfile, delimiter=",")

        for row in tweetreader:
            ft = row['time']
            hour = int(ft.split(':')[0])
            minute = int(ft.split(':')[1])
            now = datetime.datetime.now().time()
            if hour == now.hour and minute == now.minute:
                print row['text']

sched.start()
