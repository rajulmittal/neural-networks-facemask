import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import re
import time
import nltk
"# -- coding: utf-8 --"
def calctime(a):
    return time.time()-a
positive=0
negative=0
compound=0
initime = time.time()
count=0
plt.ion()
import test
ckey='F9TfrnazeR4tuG2QdyqJCgOrC'
csecret='nDzC5Bfua1IngqaGUruzGjhaABsv5y42H4g1pTSfuZh84dtbtH'
atoken='718434135925088256-3xBtFqgeH4azGXYPQ91VT7WyyyanNQp'
asecret='JcV4J6YKLXo3jljK2bx9QRD2BFBRkNoOYyNmeXkW0rZyM'

class listener(StreamListener):
    def on_data(self,data):
        global initime
        
        t= int(calctime(initime))
        all_data=json.loads(data)
        tweet=all_data["text"]
        tweet=" ".join(re.findall("[a-zA-Z]+",tweet))
        blob=TextBlob(tweet.strip())
        global positive
        global negative
        global compound
        global count
        count =count+1
        senti=0
        
        for sen in blob.sentences:
            senti=senti+sen.sentiment.polarity
            if sen.sentiment.polarity>=0:
                positive=positive+sen.sentiment.polarity
            else:
                negative=negative+sen.sentiment.polarity
            commpound=compound+senti
        print(count)
        print(tweet.strip())
        print(t)
        print(str(positive)+' '+str(negative)+' '+str(compound))
        plt.axis([0,70,-20,20])
        plt.xlabel('Time')
        plt.ylabel('Sentiment')
        plt.plot([t],[positive],'go',[t],[negative],'ro',[t],[compound],'bo') #ro go and bo are blue red greeen colors for graph
        plt.show()
        plt.pause(0.0001)
        if count==200:
            return False
        else:
            return True
    def on_error(self,status):
        print(status)
auth=OAuthHandler(ckey,csecret)
auth.set_access_token(atoken, asecret)
searchTerm=input("Enter keyword /tag to search about: ")
NoOfTerms=int(input("Enter how many tweets to search: "))
twitterStream=Stream(auth,listener(NoOfTerms))
twitterStream.filter(track=[searchTerm])