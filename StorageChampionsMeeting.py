"""
Python SDK Testing
"""

from oauthlib.oauth2 import BackendApplicationClient
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from pprint import pprint
from lxml import etree
import dscc 
#from dscc_client.rest import ApiException


def GetConnection(inputfile):
	tree = etree.parse(inputfile)
	region = tree.find('GreenLakeType').text
	if( region == 'EU'):
		baseUrl = 'https://eu1.data.cloud.hpe.com'
		clientId = (tree.find('ClientIdEU')).text
		clientSecret = (tree.find('ClientSecretEU')).text
	elif( region == 'US'):
		baseUrl = 'https://us1.data.cloud.hpe.com'
		clientId = (tree.find('ClientIdUS')).text
		clientSecret = (tree.find('ClientSecretUS')).text		
	elif( region == 'APJ'):
		baseUrl = 'https://jp1.data.cloud.hpe.com'
		clientId = (tree.find('ClientIdAPJ')).text
		clientSecret = (tree.find('ClientSecretAPJ')).text
	else:
		pprint("Unknown Region: "+region)
	
	configuration = dscc.Configuration(
    	host = baseUrl
	)
	# Get a token
	client = BackendApplicationClient(clientId)
	oauth = OAuth2Session(client=client)
	auth= HTTPBasicAuth(clientId,clientSecret)
	token = oauth.fetch_token(token_url='https://sso.common.cloud.hpe.com/as/token.oauth2', auth=auth)
	configuration = dscc.Configuration(
    	access_token = token['access_token']
	)
	return(configuration)

################## Main

configuration = GetConnection('./Credentials/dscc.xml')

with dscc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dscc.StorageSystemsApi(api_client)
    #limit = 10 # int | Number of items to return at a time (optional)
    #offset = 0 # int | The offset of the first item in the collection to return (optional)
    #filter = 'name eq VEGA_CB1507_8400_2N_150' # str | oData query to filter systems by Key. (optional)
    #sort = 'id asc,name desc' # str | Query to sort the response with specified key and order (optional)
    #select = 'id' # str | Query to select only the required parameters, separated by . if nested (optional)

    try:
        # Get all storage systems
        api_response = api_instance.systems_list()
        print("The response of StorageSystemsApi->systems_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageSystemsApi->systems_list: %s\n" % e)

