import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE tweets (keywords text, tweet_id int, tweet_text text)"

cursor.execute(create_table)

sample_tweet = ("Finally", 2398349284298123123, "Finally got outside today!")
insert_query = "INSERT INTO tweets VALUES (?, ?, ?)"
cursor.execute(insert_query, sample_tweet)

select_query = "SELECT * FROM tweets"
for row in cursor.execute(select_query):
    print(row)

connection.commit()
connection.close()