import json
from requests import request

class Authenticator:
	""""""
	GET_ACCESS_TOKEN_URL = "https://api.intra.42.fr/oauth/token"
	TEST_ACCESS_TOKEN = "https://api.intra.42.fr/oauth/token/info"
	GET_USER_DATA_URL = "https://api.intra.42.fr/v2/me"

	def __init__(self, uid, secret, redirect_uri):
		self.uid = uid
		self.secret = secret
		self.redirect_uri = redirect_uri

	def getAccessToken(self, code):
		payload = {
			'grant_type': 'authorization_code',
			'client_id': self.uid,
			'client_secret': self.secret,
			'code': code,
			'redirect_uri': self.redirect_uri
		}
		response = request("POST", Authenticator.GET_ACCESS_TOKEN_URL,data=payload)
		response = json.loads(response.text.encode('utf8'))
		print(response)
		# access_token = response.get('access_token', None)
		# return access_token
