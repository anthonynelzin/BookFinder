#!/usr/bin/env python3

"""
	Anthony Nelzin-Santos
	anthony@nelzin.fr
	https://anthony.nelzin.fr

	European Union Public License 1.2
"""

# Example ISBN from Walter Isaacson's Steve Jobs
# 1451648537
# 978-1451648539
# https://openlibrary.org/dev/docs/api/books

from ColourMatcher.colourMatcher import colourMatcher
from datetime import datetime
from ISBNChecker.ISBNChecker import ISBNChecker
import argparse
import json
import os
import re
import string
import time
import unicodedata
import urllib.request

# Retrieve metadata from the OpenLibrary API
def get_book(isbn):
	print("Retrieving metadata…")
	try:
		url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + isbn + "&jscmd=data&format=json"
		data = urllib.request.urlopen(url)
	except urllib.error.URLError:
		raise Exception("Unable to retrieve data from the Open Library. Please check your connection.")
	
	book = json.load(data)['%s:%s' % ("ISBN", isbn)]
	return book

# Create the reading log
def write_log(isbn, slug, book):
	# Create the log’s folder
	if not os.path.exists(slug):
		os.mkdir(slug)
	
	# I like verbose commands
	book_title = book.get('title', None)
	print("Title: " + book_title)
	
	book_authors = "#".join(author['name'] for author in book['authors'])
	print("Author(s): " + book_authors)
		
	book_publishers = "#".join(publisher['name'] for publisher in book['publishers'])
	print("Publisher(s): " + book_publishers)
	
	book_date = str(book.get('publish_date', None))
	print("Year: " + book_date)
	
	book_pages = str(book.get('number_of_pages', None))
	print("# of pages: " + book_pages)
	
	# Retrieve the cover… or not
	if "cover" in book:
		book_image = str(book['cover'].get('large', None))
		urllib.request.urlretrieve(book_image, slug + "/cover.jpg")
	else:
		book_image = "None"
	print("Cover: " + book_image)

	# Let's do this
	print("Creating reading log…")
	file = open(slug + "/index.md", "w")

	file.write("---\n")
	file.write("draft: true\n")
	file.write("title: \"" + book_title + "\"\n")
	file.write("description: \"" + book_title + "\"\n")
	file.write(
		"publishDate: " + datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:00+0100%z") + "\n")
	file.write(
		"date: " + datetime.now().astimezone().strftime("%Y-%m-%dT%H:%M:00+0100%z") + "\n")
	if "cover" in book:
		book_colour = colourMatcher(slug + "/cover.jpg")
		file.write("colour: \"" + book_colour + "\"\n")
	else:
		file.write("colour: \"\"\n")
	file.write("slug: " + slug + "\n")
	file.write("par: \n")
	authors = book_authors.split('#')
	for author in authors:
		file.write("- \"" + author + "\"\n")
	file.write("chez: \n")
	publishers = book_publishers.split('#')
	for publisher in publishers:
		file.write("- \"" + publisher + "\"\n")
	file.write("annee: " + book_date + "\n")
	file.write("isbn: " + isbn + "\n")
	file.write("pages: " + book_pages + "\n")
	file.write("en: \n- \"\"\n")
	file.write("dans: \n- \"\"\n")
	ile.write("de: \n- \"\"\n")
	file.write("lu: \n- \"\"\n")
	file.write("sur: \n- \"\"\n")
	file.write("---\n\n")
	file.write("## Notes\n\n## Notes archivistiques\n\n")
	
	file.close()
	print("Your reading log is ready.")
		
def main():
	parser = argparse.ArgumentParser(description="A needlessly complicated way to maintain my reading log.")
	parser.add_argument("-i", "--isbn", help="An ISBN-10 or ISBN-13.")
	parser.add_argument("-s", "--slug", help="A unique slug.")
	
	args = parser.parse_args()
	
	isbn = ISBNChecker(args.isbn)
	slug = args.slug
	book = get_book(isbn)
	write_log(isbn, slug, book)
	
if __name__ == '__main__':
	main()
