import tweepy
import json

ACCOUNT_NAME    = "josebaseba"

#Twitter API
consumer_key    = ""
consumer_secret = ""
access_key      = ""
access_secret   = ""


def downloadTweets(screen_name):

	print "Starting download..."

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)

	all_tweets = []
	new_tweets = api.user_timeline(screen_name = screen_name, count = 200)
	all_tweets.extend(new_tweets)
	oldest_tweet = all_tweets[-1].id - 1

	while len(new_tweets) > 0:
		new_tweets = api.user_timeline(screen_name = screen_name, count = 200, max_id = oldest_tweet)
		all_tweets.extend(new_tweets)
		oldest_tweet = all_tweets[-1].id - 1
		print "%s tweets downloaded..." % (len(all_tweets))

	out_tweets = [tweet.text.encode("utf-8") for tweet in all_tweets]
	parsed_tweets = dict(zip(range(len(out_tweets) + 1), out_tweets))

	with open("%s_tweets.json" % screen_name, "w") as f:
		json.dump(parsed_tweets, f, ensure_ascii = False)
	pass

if __name__ == "__main__":
	downloadTweets(ACCOUNT_NAME)

