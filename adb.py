import json
import oauth2 as oauth



API_KEY='455215929-Exmhl2w5l1LdckIkFWRoiahwmrawltGzwWQ1Mffs'

API_SECRET='elIv4IjcH9IuJNYUWwh7zbzsJJ83P5mIOEsqoQfaJ4Ri9'

CONSUMER_KEY='LmsuQDk0UNVEk0BzXDEMXVyHw'

CONSUMER_SECRET='J5QTV4bELgTH6PemoXeVkpw8y2AktHClcAVvUB27pM6NGAFbr3'


#url = 'https://api.twitter.com/1.1/account/verify_credentials.json'

consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=API_KEY, secret=API_SECRET)
client = oauth.Client(consumer, access_token)


TIMELINE_ENDPOINT = "https://api.twitter.com/1.1/statuses/home_timeline.json"
tweetsearch = "https://api.twitter.com/1.1/search/tweets.json?q=nasa&result_type=popular"
#response, data = client.request(timeline_endpoint)
response, searchin = client.request(tweetsearch)

#tweets = json.loads(data)
#for tweet in tweets:
#    print(tweet['text'])

#in1 = input("For statuses on home timeline, type home")
#in2 = input("Please type what you'd like to search for - example nasa")

#if in1 == "home":
#    url_home = "https://api.twitter.com/1.1/statuses/home_timeline.json"
#    print(url_home)

#

searchtest = json.loads(searchin)
#search = searchtest{ }
for key, value in searchtest.items():
    print(key, value)