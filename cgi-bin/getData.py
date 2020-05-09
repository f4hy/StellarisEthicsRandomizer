#!/usr/bin/env python3

# Import modules for CGI handling
import cgi
import cgitb
from randomize import generateRequiredEthic

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
empire_name = form.getvalue("empire_name")
game_id = form.getvalue("game_id")
print("Content-type:text/html")
print("")
print("Hello <br/>")
print(f"<span>Based on your empire name <b>{empire_name}</b><br/> ")
hashed, required = generateRequiredEthic(empire_name, game_id)
print(f"we are using seed <b>{hashed}</b></span><br/><br/>")
print(f"<span>You must play as: <b>{required}</b></span><br/><br/>")
print(""" <form action=".."> <input type="submit" value="Go Back" /> </form> """)
