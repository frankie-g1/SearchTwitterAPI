from flask_restful import Resource, request
import sqlite3
import tweepy


class Tweets(Resource):
    def get(self):
        keywords = request.form['see_tweets']
        if Tweets.find_by_name(keywords):
            return Tweets.find_by_name(keywords)
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

    def post(self):
        # request_data = request.get_json()
        keywords = request.form['search_tweets']
        '''  Run through the database if these words have already been searched.
             If we wanted to always be updated, we could remove this if, and new tweets
             will always be scraped from twitter regardless of repetitive keywords. '''
        #if Tweets.find_by_name(keywords):
        #    return Tweets.find_by_name(keywords)

        '''Below I must find tweets with tweepy to insert into the database'''
        # tweets_list = []
        # for tweet in tweepy.Cursor(tapi.search, q=keywords).items(10):
        #    tweets_list.append((keywords, tweet.id, tweet.text))

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        insert_query = "INSERT INTO tweets VALUES (?, ?, ?)"
        cursor.execute(insert_query, (keywords, 203102831123, "Postman"))
        # cursor.executemany(query, tweets_list)

        connection.commit()
        connection.close()

        # return {'Tweets found': tweets_list}
        return Tweets.find_by_name(keywords)
