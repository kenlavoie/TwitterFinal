import twitter

import oauth2



key=''

secret=''

CONSUMER_KEY=''

CONSUMER_SECRET=''


api = twitter.Api(consumer_key= CONSUMER_KEY,
                  consumer_secret=CONSUMER_SECRET,
                  access_token_key=key,
                  access_token_secret=secret)




home_timeline = api.GetFriends() 

#print(home_timeline)





print(home_timeline)

print([u.screen_name for u in home_timeline])
print([u.id for u in home_timeline])
