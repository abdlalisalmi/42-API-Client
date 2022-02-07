from API42Client.auth import Authenticator

UID = "38fda73983d0814a61f11848c87386074b782057e4e9572f8237a729addf2220"
SECRET = "ed48d0082d1ed323cd152711da731e3a8230ecaa2482405ee1555d748ff7d0c8"
REDIRECT_URI = "http://localhost:8000"

app = Authenticator(UID, SECRET, REDIRECT_URI)

app.getAccessToken("4fb330de16bc1824d33f5c79c96c0e1c6bc285df4adce97c4b7b6508e83de1d8")