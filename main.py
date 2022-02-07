from API42Client.auth import Authenticator

UID = "38fda73983d0814a61f11848c87386074b782057e4e9572f8237a729addf2220"
SECRET = "ed48d0082d1ed323cd152711da731e3a8230ecaa2482405ee1555d748ff7d0c8"
REDIRECT_URI = "http://localhost:8000"

app = Authenticator(UID, SECRET, REDIRECT_URI)

token = app.get_Access_token(
        "e3aa00607eda684c5b3722856c52f714c9896c7e94d3c9c81123b39cbd764ce7")
isValid = app.is_valid_token("c7572b89d479c4ea3cd9b5de11540c3f54be8b861d75610fe65084697c26b284")
print(isValid)

test = {
    'access_token':
    'c7572b89d479c4ea3cd9b5de11540c3f54be8b861d75610fe65084697c26b284',
    'token_type': 'bearer',
    'expires_in': 7200,
    'refresh_token':
    '6132a231350122da051f0a09c5c7598040f40751f56952cad96077b70156ba5b',
    'scope': 'public',
    'created_at': 1644261471
}
