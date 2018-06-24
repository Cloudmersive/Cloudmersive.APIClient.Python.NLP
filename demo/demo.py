from __future__ import print_function
import time
import cloudmersive_nlp_api_client
from cloudmersive_nlp_api_client.rest import ApiException
from pprint import pprint



# create an instance of the API class
api_instance = cloudmersive_nlp_api_client.ExtractEntitiesStringApi()
value = 'A co-owner of the Red Hen in Lexington, Virginia, asked Ms Sanders and her family to leave as a protest against the Trump administration.' # str | Input string

api_instance.api_client.configuration.api_key = {}
api_instance.api_client.configuration.api_key['Apikey'] = '04d1a7be-c9d1-4d93-8ec4-e7545c2a570a'

try:
    # Extract entities from string
    api_response = api_instance.extract_entities_string_post(value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ExtractEntitiesStringApi->extract_entities_string_post: %s\n" % e)