import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, SentimentOptions

#Send a get request to a specified url
def get_request(url, **kwargs):
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        if 'api_key' in kwargs:
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs, auth=HTTPBasicAuth('apikey', kwargs['api_key']))
        else:
            response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
        return None

    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

#Return a list of dealer objects
def get_dealers_from_cf(url):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results

#Return list of dealer review objects
def get_dealer_reviews_from_cf(url, dealer_id):
    result = []
    json_result = get_request(url, id=dealer_id)

    if json_result:
        reviews = json_result
     
        for review in reviews:
            review['sentiment'] = analyze_review_sentiments(review['review'])
            review_obj = DealerReview(review)
            result.append(review_obj)
            
    return result

#Analyze sentiment for the review
def analyze_review_sentiments(dealer_review):

    authenticator = IAMAuthenticator('iNkqkgBR2vmKDQQ1Ve-N-283-ltPJbhLgFmJ_EGHUXaB')
    natural_language_understanding = NaturalLanguageUnderstandingV1(version='2022-04-07', authenticator=authenticator)
    natural_language_understanding.set_service_url('https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/e622df82-44f8-439c-ba8d-9a3365aea640')

    response = natural_language_understanding.analyze(
    text = dealer_review,
    return_analyzed_text = True,
    language = 'en',
    features=Features(
        sentiment=SentimentOptions()
    )).get_result()

    return response['sentiment']['document']['label']


def post_request(url, json_payload):
    response = request.post(url, json=json_payload)
    return response
