import os
import time
import classinput
import twttr1
import json
#import flask
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)   # create our flask app


#@app.route('/') 
#def twitterform(): 
#   return render_template('twitterform.html')



@app.route('/', methods=['GET'])
def landingpage():

    APIKEY=''

    APISECRET =''

    CONSUMERKEY =''

    CONSUMERSECRET=''

    aut = twttr1.Auth()
    client = aut.runauth(APIKEY, APISECRET, CONSUMERKEY, CONSUMERSECRET)

    ci = classinput.UserReq()

    input11 = raw_input("For home timeline, type home: ")
    input22 = raw_input("Type something to search for, no # needed: ") 
    input33 = raw_input("Type a user to search for: ")


    #print(ci.home_timeline(input11, client))
    #print(ci.tweet_search(input22, client))
    #print(ci.user_timeline(input33, client)) 
    inputone =  ci.user_timeline(input11, client) 
    newinputone = json.dumps(inputone)
    return jsonify(newinputone)  

    inputtwo =  ci.user_timeline(input22, client) 
    newinputtwo = json.dumps(inputtwo)
    return jsonify(newinputtwo)  

    inputthree =  ci.user_timeline(input33, client) 
    newinputthree = json.dumps(inputthree)
    return jsonify(newinputthree)  

