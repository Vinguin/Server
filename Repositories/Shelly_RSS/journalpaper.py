#!/usr/bin/python
# -*- coding: iso-8859-1 -*-

from lxml import html, cssselect
import requests
import os
import time

url2check = "http://journals.aps.org/prl/"


# Speichert die aktuelle HTML in die Datei "output.txt"
def save_html_to_file():
    ofile = open("output.txt", "w")
    for title in get_title_list():
        ofile.write(title+"\n".encode('utf8'))
    ofile.close()
    print "Aktualisiere output.txt"


# Ueberpruefe, ob sich was geaendert hat.
def website_has_changed():
    has_changed = False
    ifile = open("output.txt", "r")
    saved_list = map(str.rstrip, ifile.readlines())
    ifile.close()

    changefile = open("new_titles.txt", "w")

    for title in get_title_list():
        if title not in saved_list:
            changefile.write(title+"\n".encode('utf8'))
            has_changed = True
    changefile.close()

    return has_changed


# Scrape die aktuelle Titelliste von der Website.
def get_title_list():
    newTitleList = []
    page = requests.get(url2check)
    tree = html.fromstring(page.content)
    title_a = tree.cssselect("h4.title a")
    for title in title_a:
        newTitleList.append(title.text.encode('utf8'))

    return map(str.rstrip, newTitleList)


def initiate():
    try:
        file = open("output.txt", "r")
    except IOError:
        print "Lege neue Datei an"
        save_html_to_file()

    if len(file.read()) == 0:
        save_html_to_file()
        print "Initialisiert"


# Sende eine Benachrichtigungsmail.
def sendmail():
    os.system("python sendmail.py")


def main():
    initiate()
    if website_has_changed():
        print "Änderung auf:" + url2check
        sendmail()
        save_html_to_file()
    else:
        print time.strftime("%a, %d %b %Y - %X") + \
            "\tKeine Aenderung auf " + url2check

if __name__ == "__main__":
    main()




