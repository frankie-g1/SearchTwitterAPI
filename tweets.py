from flask import render_template
from flask_table import Table, Col
from flask_restful import Resource, request
import sqlite3
import json
import tweepy


class Tweets(Resource):


    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM tweets"
        result = cursor.execute(select_query)
        row = result.fetchall()
        connection.close()
        if row:
            return result
        return {'message': ' Item not found'}, 404

    @classmethod
    def find_by_name(cls, keywords):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "SELECT * FROM tweets WHERE keywords=?"

        result = cursor.execute(select_query, (keywords,))
        row = result.fetchall()
        connection.close()
        if row:
            return {'Tweets': row}

    @classmethod
    def delete_by_name(cls, keywords):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        select_query = "DELETE FROM tweets WHERE keywords=?"

        result = cursor.execute(select_query, (keywords,))
        row = result.fetchall()
        connection.close()
        if row:
            return True

    def post(self):
        # request_data = request.get_json()
        keywords = request.form['search_tweets']
        '''  Run through the database if these words have already been searched.
             To return a recent list of tweets -> remove this old tweets from past
             user submissions and continue to use Twitter API again '''
        #  Used to return tweets from a previous user submission, now we
        #  perform n more SQL operations by deleting those tweets.
        #  The extra computing time keeps the database size to a minimum
        if Tweets.find_by_name(keywords):
            Tweets.delete_by_name(keywords)

        '''Below I must find tweets with tweepy to insert into the database'''
        auth = tweepy.AppAuthHandler(consumer_key="p7ZaeOKcUmWMCqPgoVwC9RjLt",
                                     consumer_secret="uKsseakqpOmyhtrssQvbGPcRffi9ALrsdIjLt90YbpfE9SXklz")
        t_api = tweepy.API(auth)
        tweets_list = []
        for tweet in (t_api.search_30_day("SearchTwitterAPI", keywords, [10])):
            tweets_list.append((keywords, tweet.id, tweet.text))



        '''Here is a database insert regarding only to the form's text field.
            This is placeholder until Twitter API access.
        '''
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        insert_query = "INSERT INTO tweets VALUES (?, ?, ?)"
        for row in range(0, len(tweets_list)):
            cursor.execute(insert_query, (tweets_list[row]))

        connection.commit()
        connection.close()

        #with open('templates/tweets.json', 'w') as fp:
        #    json.dump(Tweets.find_by_name(keywords), fp, sort_keys=True, indent=4)
        # return {'Tweets found': tweets_list}
        return {'Tweets found': Tweets.find_by_name(keywords)}, 201

