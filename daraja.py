import requests
CONSUMER_KEY = "nQaE14QbZp9U3IaEsObGHEgGMy3gws4CFAtlBvImzsQBsWRwYJMWfV587zsGQoQ8dW7N9BcXrfAuoRRbGkAtp06tHK9Vb0lGxPhFLSwZD0jJXGQA"
CONSUMER_SECRET = "YJMWfV587zsGQoQ8dW7N9BcXrfAuoRRbGkAtp06tHK9Vb0lGxPhFLSwZD0jJXGQA"

def get_token():
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(url, auth=(CONSUMER_KEY, CONSUMER_SECRET))
    print(r.json())
