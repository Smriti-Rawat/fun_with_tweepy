import tweepy
import time
from authentication.Basic_auth import auth

# If the authentication was successful, you should
# see the name of the account print out
api=auth()

# We use pagination a lot in Twitter API development. 
# Iterating through timelines, user lists, direct messages, etc. 
# In order to perform pagination we must supply a page/cursor parameter with each of our requests. The problem here is this requires 
# a lot of boiler plate code just to manage the pagination loop. To help make pagination easier and require less code Tweepy has the Cursor object.

followers = []
for follower in tweepy.Cursor(api.followers).items():
	followers.append(follower)

friends = []
for friend in tweepy.Cursor(api.friends).items():
	friends.append(friend)

# now we find all your "non_friends" - people who don't follow you
# even though you follow them.
friend_dict = {}
for friend in friends:
	friend_dict[friend.id] = friend

follower_dict = {}
for follower in followers:
	follower_dict[follower.id] = follower

non_friends = [friend for friend in friends if friend.id not in follower_dict]

# print "people who don't follow you back: \n" 

# for nf in non_friends:
# 	print nf.screen_name

print "Unfollowing %s people who don't follow you back" % len(non_friends)

for nf in non_friends:
	print "Unfollowing %s" % nf.screen_name
	try:
		nf.unfollow()
	except:
		print "  .. failed, sleeping for 5 seconds and then trying again."
		time.sleep(5)
		nf.unfollow()
	print " .. completed, sleeping for 1 second."
	time.sleep(1)







