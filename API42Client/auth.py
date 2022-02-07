import json
from requests import request


class Authenticator:
	"""
	Authenticator
	
	The Authenticator make you connect to the 42 School API with the Authorization Code flow,
	this step for geting the Access-token That access token is used by the client to make API calls.
	
	Options:
	  - `uid`      		:	your 42 application's UID
	  - `secret`  		:	your 42 application's SECRET
	  - `redirect_uri`  : 	URL to which 42 will redirect the user after granting authorization
	"""

	GET_ACCESS_TOKEN_URL = "https://api.intra.42.fr/oauth/token"
	TEST_ACCESS_TOKEN = "https://api.intra.42.fr/oauth/token/info"
	GET_USER_DATA_URL = "https://api.intra.42.fr/v2/me"

	def __init__(self, uid, secret, redirect_uri):
		self.uid = uid
		self.secret = secret
		self.redirect_uri = redirect_uri

	def get_Access_token(self, code):
		""""""
		payload = {
			'grant_type': 'authorization_code',
			'client_id': self.uid,
			'client_secret': self.secret,
			'code': code,
			'redirect_uri': self.redirect_uri
		}
		res = request("POST", Authenticator.GET_ACCESS_TOKEN_URL, data=payload)
		return json.loads(res.text.encode('utf8'))

	def is_valid_token(self, access_token):
		""""""
		res = request("GET",
					  Authenticator.TEST_ACCESS_TOKEN,
					  headers={'Authorization': f'Bearer {access_token}'})
		return True if res.status_code == 200 else False
