import tweepy
import time

auth = tweepy.OAuthHandler('HclONosamerxnuJ5S8U88AOmK',
                           'OBpETBSdaEFD9PvVhYRfpZh40YkuPobT6u37qmVZKm3xwyd4Ln')
auth.set_access_token('1257312720040292360-nlvj31Ro8J6Xd0R8XbCUW5oCnBKBtt',
                      'BhHOMdy6itb67B85N4rJOAHQDN2Mk7vk03x5dXq1FP2rs')

api = tweepy.API(auth)

public_tweets = api.home_timeline()

""" for tweet in public_tweets:
    print(tweet.text)
user = api.me()
print(user.followers_count)
print(user)
print(user.screen_name)
 """
def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)

       
#generous bot 
""" for follower in limit_handler(tweepy.Cursor(api.followers).items()):
    if follower.name == 'ajax':
        follower.follow()
        break

 """
search_string  = 'shivangi'
numberoftweets =2

for tweet in tweepy.Cursor(api.search,search_string).items(numberoftweets):
    try:
        tweet.favorite()
        print('i liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break