#!/usr/bin/env python3
"""
cmyip_cli.py: A command line utility to parse data from cmyip.com
"""
__author__     = "Olivia Mackintosh"
__email__      = "livvy@protonmail.com"
__copyright__  = "Copyright 2016, Olivia Mackintosh"
__licence__    = "GPL-3.0"

import bs4
import pprint
import requests

url = "http://cmyip.com/"

# Make the request to cmyip.com using the requests library
# before getting just the text only.
response = requests.get(url)
text = response.text

# Create a BeautifulSoup object while explicitly stating
# which parser BeautifulSoup should use. This is to avoid
# errors from any future changes to the library.
soup = bs4.BeautifulSoup(text, "html.parser")

# Remove 'a' and 'img' tags from the tree.
for crud in soup.body.find_all(["a", "img"]):
    crud.decompose()

# Get the main data containing objects that have the
# class attribute 'page-title'.
tags = soup.find_all(class_='page-title')

# Get only the tags' contents from the new list and
# add them to a new list called attributes after
# removing trailing whitespace.
attributes = []
for content in tags:
    attributes.append(content.get_text().rstrip())

# Pretty print the attributes
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(attributes)
