#!/home/protected/venv/bin/python


# Import modules for CGI handling
import cgi
import cgitb
from randomize import generateRequiredEthic
from pathlib import Path
from steamsignin import SteamSignIn

from steam.client import SteamClient

cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
steam_id = form.getvalue("steam_id")
# print("Content-type:text/html")
# print("")
# print("Hello <br/>")

steamLogin = SteamSignIn()
redirect = steamLogin.RedirectUser(
    steamLogin.ConstructURL("http://stellaris.f4hy.net/cgi-bin/show_steam_info.py")
)
# ForwardClientToSteamPage(encodedData) #Not a real function, but the next action you'd take

print(redirect)
# returnedSteamID = steamLogin.ValidateResults(encodedData)
# print(returnedSteamID)

# client = SteamClient()
# session = client.get_web_session()
# print(session)
# cookies = client.get_web_session_cookies()
# print(session)
