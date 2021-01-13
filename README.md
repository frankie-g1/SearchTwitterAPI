# SearchTwitterAPI

Future plans:
  Implement Twitter API + Tweepy to return the tweets found through the submit fields keywords.

 [Currently:](https://imgur.com/a/invOBNb)
  Without Twitter API access, the API's post method inserts the tuple (user's filters, fake tweet id 203102831123, and fake tweet text "Postman") into the sqlite3 database.
  
  
  Side note a GET method, returning previously scraped tweets isn't ready yet. I need to read up on Flask's documentation to have the API understand requests with the route /tweets?see_tweets=user's filters 
  
  

