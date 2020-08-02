#!/home/protected/venv/bin/python


# Import modules for CGI handling
import cgi
import cgitb
from randomize import generateRequiredEthic
from pathlib import Path
from steamsignin import SteamSignIn

from components import create_dropdown
from gamesettings import get_ranges

# from steam.client import SteamClient
from steam.webapi import WebAPI

cgitb.enable()
# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
# steam_id = form.getvalue("steam_id")
print("Content-type:text/html")
print("")
print("Hello <br/>")

d = {}
for i in form.keys():
    d[i] = form.getvalue(i)

# print(d)
steamLogin = SteamSignIn()
returnedSteamID = steamLogin.ValidateResults(d)
print(returnedSteamID)

api = WebAPI(key="9819B8A5C2FAF7893682425E53EF4C06")

response = api.ISteamUser.GetPlayerSummaries(steamids=returnedSteamID)
player_info = response["response"]["players"][0]

print(f"Welcome: {player_info.get('personaname')}")
print(f"<img src='{player_info.get('avatarmedium')}' />")
# client = SteamClient()
# session = client.get_web_session()
# print(session)
# cookies = client.get_web_session_cookies()
# print(session)

print("<form action='cgi-bin/generate.py'>")
ranges = get_ranges("medium")
for name, options in ranges.items():
    print(create_dropdown(name, options))
print("<input type='submit'>")
print("</form>")
