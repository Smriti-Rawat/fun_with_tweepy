import tweepy
from authentication.Basic_auth import auth


api=auth()

# If the authentication was successful, you should
# see the name of the account print out
# print(api.me().name)

user = api.get_user('iamsmriti3')
print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name