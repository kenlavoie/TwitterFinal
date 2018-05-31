import classinput
import twttr1

APIKEY=''

APISECRET =''

CONSUMERKEY =''

CONSUMERSECRET=''

aut = twttr1.Auth()
client = aut.runauth(APIKEY, APISECRET, CONSUMERKEY, CONSUMERSECRET)

ci = classinput.UserReq()

input11 = raw_input("For home timeline, type home: ")
input22 = raw_input("Type something to search for, no # needed")
input33 = raw_input("Please enter a user to search for")

print(ci.home_timeline(input11, client))
print(ci.tweet_search(input22, client))
