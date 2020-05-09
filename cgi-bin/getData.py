#!/usr/bin/env python3

# Import modules for CGI handling
import cgi, cgitb
from randomize import generateRequiredEthic

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
empire_name = form.getvalue("empire_name")
game_id = form.getvalue("game_id")
print("Content-type:text/html")
print("")
print("")
print("Hello ")
print("")
print("")
generateRequiredEthic(empire_name, game_id)
print("")
