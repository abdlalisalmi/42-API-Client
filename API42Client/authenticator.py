

class Authenticator:
	""""""
	def __init__(self, uid, secret):
		self.uid = uid
		self.secret = secret

	def getAccessToken(self):
		print("Get Token Method")
