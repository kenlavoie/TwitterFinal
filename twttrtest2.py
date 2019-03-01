import requests 
import json
import requests
import oauth2 as oauth
#from requests_oauthlib import OAuth1, OAuth2

API_KEY=''

API_SECRET=''

CONSUMER_KEY=''

CONSUMER_SECRET=''
"""
consumer = oauth.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
access_token = oauth.Token(key=API_KEY, secret = API_SECRET)
client.oauthClient(consumer, access_token)

timeline_endpoint = "https://api.twitter.com/1.1/statuses/home_timeline.json"
response, data = client.request(timeline_endpoint)

tweets = json.loads(data)
for tweet in tweets:Exmhl2w5l1LdckIkFWRoiahwmrawltGzwWQ1Mffs
    print(tweet['text'])
"""

def oauth_req(url, key, secret, http_method="GET", post_body="WHAT", http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=API_KEY, secret=API_SECRET)
    client = oauth2.Client(consumer, token)
    resp, content = client.request( url, method=http_method, body=post_body, headers=http_headers )
    return(content)



home_timeline = oauth_req( 'https://api.twitter.com/1.1/statuses/home_timeline.json', API_KEY, API_SECRET  )

"""
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1(API_KEY, API_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
requests.get(url, auth=auth)

r = requests.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=stackoverflow&count=100', auth=auth)
#for tweet in r.json():
print(r)

"""

"""
API_KEY='455215929-Exmhl2w5l1LdckIkFWRoiahwmrawltGzwWQ1Mffs'

API_SECRET='elIv4IjcH9IuJNYUWwh7zbzsJJ83P5mIOEsqoQfaJ4Ri9'

CONSUMER_KEY='LmsuQDk0UNVEk0BzXDEMXVyHw'

CONSUMER_SECRET='J5QTV4bELgTH6PemoXeVkpw8y2AktHClcAVvUB27pM6NGAFbr3'

api = twitter.Api(consumer_key= CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=key,
                  access_token_secret=secret)




home_timeline = api.GetFriends() 
#print(home_timeline)





print(home_timeline)

print([u.screen_name for u in home_timeline])
print([u.id for u in home_timeline])

"""
