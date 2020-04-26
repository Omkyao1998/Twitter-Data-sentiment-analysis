import tweepy
from textblob import TextBlob

#Authenticating and accessing Twitter API
consumerkey = '#Your Key'
consumersecret = '#Your Customer Secret key'
acctoken = '#Your access token'
acctokensec = '#your secret token'	
auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(acctoken, acctokensec)
api = tweepy.API(auth)

#Searching Tweets related to our search Like here Covid-19	
public_tweets = api.search('Covid-19')

#for fetching tweets and finding sentiments	
for tweets in public_tweets:
	analysis = TextBlob(tweets.text)
	print(analysis.sentiment)
	print(tweets.text)
		
	if analysis.sentiment[0]>0:
		print ('Positive')
		pt = tweets.text
	elif analysis.sentiment[0]<0:
		print ('Negative')
		ntw = tweets.text
	else:
		print ('Neutral')
		ne = tweets.text

#finding percentage of the sentiments found		
p = len(pt)
n = len(ntw)
ns = len(ne)
total = p + n + ns
positivepercent = (p/total)*100
print('Positive Percentage:')
print(positivepercent)
negativepercent = (n/total)*100
print('Negative Percentage:')
print(negativepercent)
neutralpercent = (ns/total)*100
print('Neutral Percentage:')
print(neutralpercent)		
