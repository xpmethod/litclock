import csv
import time
import datetime

# open takes the name of the file and modes like read and write
with open('test.csv', 'r') as csvfile:
    tweetreader = csv.DictReader(csvfile, delimiter=",")

    for row in tweetreader:
        ft = row['time']
        hour = int(ft.split(':')[0])
        minute = int(ft.split(':')[1])
        now = datetime.datetime.now().time()
        # import pdb; pdb.set_trace();
        if hour == now.hour and minute == now.minute:
            print row['text']
