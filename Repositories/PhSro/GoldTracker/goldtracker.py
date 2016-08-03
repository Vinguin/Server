#!/usr/bin/python

import mechanize

# Create a browser object
br = mechanize.Browser()
br.addheaders = [('User-agent', 'Firefox')]

br.open("https://sro.projecthax.com/")


br.select_form(nr=0)
br.form.controls[0] = "bubchen"
br.form.controls[1] = "vn831993"

response = br.submit()
print response.read()

