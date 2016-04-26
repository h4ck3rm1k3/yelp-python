
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator

auth = Oauth1Authenticator(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    token=token,
    token_secret=token_secret
)

client = Client(auth)
import pprint

o = open ("found.py","w")
for x in range(0,1000):
    params = {
        'term': 'food',
        'lang': 'en',
        'offset' : x * 10,
        'limit' : 10
        }
    x = client.search('Trenton', **params)
    for y in x.businesses:
        o.write(
            pprint.pformat(
                { 
                    'main':  y.__dict__,
                    'loc' :  y.location.__dict__,
                'coord': y.location.coordinate.__dict__ ,
                    }
                ) + "\n"
            )
        
