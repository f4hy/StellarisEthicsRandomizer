#!/usr/bin/env python3

# Import modules for CGI handling
import cgi
import cgitb
from randomize import generateRequiredEthic
from pathlib import Path

# Create instance of FieldStorage
form = cgi.FieldStorage()
# Get data from fields
steam_id = form.getvalue("steam_id")
game_id = form.getvalue("game_id")
print("Content-type:text/html")
print("")
print("Hello <br/>")
print(f"<span>Based on your empire name <b>{steam_id}</b><br/> ")
hashed, required, img = generateRequiredEthic(steam_id, game_id)
tag = hashed[:4]
path = Path(f"./{game_id}_{tag}")
with open(path, "w") as f:
    f.write(f"{steam_id}\n")
    f.write(f"{required}\n")
    f.write(img)
print(f"we are using seed <b>{hashed}</b></span><br/><br/>")
print(f"<span>You must play as: <b>{required}</b><img src='{img}'/></span><br/><br/>")
print(
    f"<span>Build your strategy around being the above choice. All other decisions are yours.</span><br/><br/>"
)
print(f"<span>Please put : <b>{tag}</b> at the end of your empire name<br/><br/>")

print(""" <form action=".."> <input type="submit" value="Go Back" /> </form> """)
