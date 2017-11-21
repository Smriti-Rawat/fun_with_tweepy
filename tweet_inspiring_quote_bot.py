import tweepy ,json ,requests ,time 
from authentication.Basic_auth import auth


api=auth()
api_url="https://random-quote-generator.herokuapp.com/api/quotes/random"

def get_quotes():
	response = requests.get(api_url)
	random_quote=json.loads(response.content)
	return random_quote['quote']


def tweet_quote():

	for i in range(1, 10):
		quote = get_quotes()
		time.sleep(30)
		try:
			api.update_status(quote)  # This method is accessed in tweepy
			print('Done')
		except tweepy.error.TweepError:
			pass


if __name__ == '__main__':
	tweet_quote()