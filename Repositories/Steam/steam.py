#/usr/bin/python3

from lxml import html, cssselect
import requests


steam_api_key = '6DCDB66D280F81DFDB0644055CDFD6F2'

# Meine Output-Datei
ofile = open("output.txt", "w")

def getMatchHistory(steamkey):
    page = requests.get("https://api.steampowered.com/IDOTA2Match_570/" +
                    "GetMatchHistory/V001/?key=" + steamkey)
    tree = html.fromstring(page.content)

    print (result.text)



