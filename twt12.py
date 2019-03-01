import json
import oauth2 as oauth



API_KEY=''

API_SECRET=''

CONSUMER_KEY=''

CONSUMER_SECRET=''


#url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=API_KEY, secret=API_SECRET)
client = oauth.Client(consumer, access_token)

#timeline_endpoint= "https://api.twitter.com/1.1/statuses/home_timeline.json"
#tweetsearch = "https://api.twitter.com/1.1/search/tweets.json?q="
#response, data = client.request(timeline_endpoint)
#response, searchin = client.request(tweetsearch)
#"https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular"

#tweets = json.loads(data)
#for tweet in tweets:
#    print(tweet['text'])



in1 = input("For statuses on home timeline, type home: ")

in2 = input("Please type what you'd like to search for - example nasa")

upin2 = "{}&result_type=popular".format(in2)

search = "https://api.twitter.com/1.1/search/tweets.json?q={}".format(upin2)



if in1 == "home":
    url_home = "https://api.twitter.com/1.1/statuses/home_timeline.json"
    print(url_home)

search = "https://api.twitter.com/1.1/search/tweets.json?q={}".format(upin2)

#url2_home = ] ""

searchtest = json.loads(searchin)
#search = searchtest{ }
for key, value in searchtest.items():
    print(key, value)
#for tweet in searchtest:
#    print(tweet['text'])
