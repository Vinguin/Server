#/usr/bin/python3

from lxml import html, cssselect
import requests


# Meine Output-Datei
ofile = open("output.txt", "w")

page = requests.get("https://sro.projecthax.com/")
tree = html.fromstring(page.content)

result = tree.cssselect("table.table td")[1]
print (result.text)



