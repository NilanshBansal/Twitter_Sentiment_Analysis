from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
import sentiment_mod as s


#consumer key, consumer secret, access token, access secret.
ckey='VE8ku9Jb66KaLFbydxsVYVVAJ'
csecret='G8wC7DrcKGuwl04n35HriXon0ig0dgVclQKqJuj7rb4sLtIavr'
atoken='3372431615-M6FVyUITANTAD3acYv9V9gYf0ePEM8kQCWaePIM'
asecret='EyDYdsbf2Jc6bq9VFs5X5M4zr1BDuLyQ02DHWS5NY9Ih1'

class listener(StreamListener):

    def on_data(self, data):
        try: 
            all_data = json.loads(data)

            tweet = ascii(all_data["text"])
            sentiment_value,confidence = s.sentiment(tweet)

            print(tweet,sentiment_value,confidence)

            if confidence*100 >= 80:
                output = open("twitter-out.txt","a")
                output.write(sentiment_value)
                output.write("\n")
                output.close()
            return True
        except:
            return True

    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["happy"])