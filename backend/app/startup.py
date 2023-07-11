from  app.spotify_auth import getAuth, refreshAuth, getToken
from app import app

#Add your client ID
CLIENT_ID = "d7370234cf774747b12adc9872ffc05c"

#aDD YOUR CLIENT SECRET FROM SPOTIFY
CLIENT_SECRET = "c9c1b0a4ccab49f881ce4f392212d199"

#Port and callback url can be changed or ledt to localhost:5000
PORT = "5000"
CALLBACK_URL = "http://localhost"

#Add needed scope from spotify user
SCOPE = "streaming user-read-email user-read-private user-read-playback-state "
#token_data will hold authentication header with access code, the allowed scopes, and the refresh countdown 
TOKEN_DATA = []


def getUser():
    return getAuth(CLIENT_ID, "{}:{}/callback/".format(CALLBACK_URL, PORT), SCOPE)

def getUserToken(code):
    global TOKEN_DATA
    TOKEN_DATA = getToken(code, CLIENT_ID, CLIENT_SECRET, "{}:{}/callback/".format(CALLBACK_URL, PORT))
 
def refreshToken(time):
    time.sleep(time)
    TOKEN_DATA = refreshAuth()

def getAccessToken():
    return TOKEN_DATA
