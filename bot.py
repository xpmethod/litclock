import csv

# open takes the name of the file and modes like read and write
with open('tweets.csv', 'r') as csvfile:
    tweetreader = csv.reader(csvfile, delimiter=",")
    for row in tweetreader:
        print row
