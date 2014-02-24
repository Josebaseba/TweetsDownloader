TweetsDownloader
================

Download lastest tweets from anyone twitter account and create a JSON file with the tweets. Twitter only lets to download until 3500 tweets, but in my case is enough so...

To use this script you need to install tweepy python package, download instructions here:

  https://github.com/tweepy/tweepy
  
Download the script and change the ACCOUNT_NAME variable name. For example:

  ACCOUNT_NAME = "josebaseba"

Remember that you have to create an twitter developer application to get the necessary keys, here the link:

  https://apps.twitter.com/
  
When you create the application you can get the keys when you click in the "Test OAuth" button. Change in the script the variables values. For example:

  consumer_key    = "8zkwSodjBTTdLoNlQrhfw"
  consumer_secret = "B07QzivDHNtQIyxYJTTIlf05z8lcGnI9Q95MTCLTQCW0"
  access_key      = "301674894-rUG4PSlCtTTOPnIcjjRwijPWgKQpwqJfq7bP5r0s"
  access_secret   = "tGMLqQzC6r9EtncWznRY3VTT5s22h8j9e0scB7SVCtRVc"
  
After that you only have to run the python script executing this shell command:

  python tweets_downloader.py
  
A .json will be created in the same folder that you run the script.

Enjoy!!


