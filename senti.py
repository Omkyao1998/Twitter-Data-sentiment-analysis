import tweepy
from textblob import TextBlob

#Authenticating and accessing Twitter API
consumerkey = 'T7THdDCzjyoWDnOkxxIcZ1WYx'
consumersecret = 'ydUIwpx5ddf8LnKsTp1rRBVQQUW44DHPi4xvQ2b0ORPhv2TVxp'
acctoken = '1016722022179725315-t0xpiyvHe1iyJ4gKz0DkZLoJvRrxHa'
acctokensec = 'Ma0BOobgdmULYrBvDYAlHOtKsOlvdP8GDwuu4x0yBka5R'	
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
