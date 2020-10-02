import tweepy

# Authenticate to Twitter
Api_key = "VYjNpc4so7mwUCNzhfh5f53097231"
Secret_key = "zhz5eUGsOfbRpOaJiSCufLo9yTJoXla7ZYxcaA3lan2VzvrolU1234"

auth = tweepy.OAuthHandler(Api_key, Secret_key)

Access_token ="1169466319130873856-aqli28WBrNS2dyNngg0GL4qMSaXT7Y"
Access_key = "SHGtkptotmM4gnFsZXGp5Kp497sFSUswBD6wzrwLmJlrb"

auth.set_access_token(Access_token, Access_key)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

"""-------------------Code Snippets for ALL methods of TWITTER-------------------------------------------------------"""

# get the last 20 entries in your timeline.
"""timeline = api.home_timeline()
for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")

# creating tweet
api.update_status("Test tweet from Tweepy Python")"""


# Fetch user from twitter
"""
user_twitter = api.get_user("@anil_kanta")
print(user_twitter.screen_name)
print(user_twitter.name)
print(user_twitter.location)
print(user_twitter.description)

for i in user_twitter.followers():
    print(i.screen_name)
"""
# for following someone
"""
api.create_friendship("whom_you_want_follow")"""

# for updating Profile description
"""
api.update_profile(description="add_things_want")"""

# home_timeline() to get the most recent tweet. Then, the tweet.id is passed to create_favorite() to mark the tweet as Liked.
"""
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)
"""

# for block users
"""
for block in api.blocks():
    print(block.name)
    """

#for searching tweets
"""
for i in api.search(q="python",lang="en", rpp=10):
    print(f"Name:{i.user.name}\nText:{i.text}")
    """

# list the world-wide trending topics:
"""
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])
"""

# see the full list of available locations using
"""print(api.trends_available())
"""

#fetch every tweet in which you are mentioned, and then mark each tweet as Liked and follow its author
"""
tweets = api.mentions_timeline()
for tweet in tweets:
    tweet.favorite()
    tweet.user.follow()"""

# only the first page from your timeline, but also the last 100 tweets:
"""
for tweet in tweepy.Cursor(api.home_timeline).items(100):
    print(f"{tweet.user.name} said: {tweet.text}")"""
