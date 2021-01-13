from flask import Flask, render_template, request
from flask_restful import Api
import tweepy
from tweets import Tweets

import tweepy
import sqlite3

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home_search():
    return render_template('search_tweets.html')


api.add_resource(Tweets, '/tweets')
if __name__ == '__main__':
    app.run(port=5000, debug=True)
