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

from datetime import datetime
import argparse
import json
import os
import string
import unicodedata
import urllib.request

# Clean the provided ISBN
def isbn_clean(isbn):
	return isbn_cleaned = re.sub("\W", "", isbn)

# Retrieved metadata from the OpenLibrary API
def get_book(isbn):
	url = "https://openlibrary.org/api/books?bibkeys=ISBN:" + isbn + "&jscmd=data&format=json"
	#print(url)
	oldata = urllib.request.urlopen(url)
	book = json.load(oldata)['%s:%s' % ("ISBN", isbn)]
	#print(book)
	return book

# Create the reading log
def reading_notes_generator(isbn, slug, book):
	print("Creating reading log…")

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
	
	if "cover" in book:
		book_image = str(book['cover'].get('large', None))
		print("Cover: " + book_image)

	# Let's do this
	if not os.path.exists(slug):
		os.mkdir(slug)
	file = open(slug + "/index.md", "w")
	file.write("---\n")
	file.write("draft: true\n")
	file.write("title: \"" + book_title + "\"\n")
	file.write(
		"publishDate: " + datetime.now().strftime("%Y-%m-%dT%H:%M:%S" + "+01:00") + "\n")
	file.write(
		"date: " + datetime.now().strftime("%Y-%m-%dT%H:%M:%S" + "+01:00") + "\n")
	file.write("theme: \"\"\n")
	file.write("slug: " + slug + "\n")
	file.write("auteurs: \n")
	authors = book_authors.split('#')
	for author in authors:
		file.write("- \"" + author + "\"\n")
	file.write("editeurs: \n")
	publishers = book_publishers.split('#')
	for publisher in publishers:
		file.write("- \"" + publisher + "\"\n")
	file.write("annee: " + book_date + "\n")
	file.write("pages: " + book_pages + "\n")
	file.write("isbn: " + isbn + "\n")
	file.write("pays: \n")
	file.write("achatDate: \"\"\n")
	file.write("achatLieu: \"\"\n")
	file.write("achatPrix: \"\"\n")
	file.write("lectures: \n- \"\"\n")
	file.write("cotes: \n- \"\"\n")
	file.write("genres: \n- \"\"\n")
	file.write("themes: \n- \"\"\n")
	file.write("---\n\n")
	file.write("## Notes\n\n## Notes archivistiques\n\n")
	
	file.close()

	if "cover" in book:
		urllib.request.urlretrieve("" + book_image, slug + "/cover.jpg")

	print("Your reading log is ready.")
		
def main():
	parser = argparse.ArgumentParser(description="A needlessly complicated way to maintain my reading log.")
	parser.add_argument("-i", "--isbn", help="An ISBN-10 or ISBN-13.")
	parser.add_argument("-s", "--slug", help="A unique slug.")
	
	args = parser.parse_args()
	
	isbn = isbn_clean(args.isbn)
	slug = args.slug
	book = get_book(isbn)
	reading_notes_generator(isbn, slug, book)
	
if __name__ == '__main__':
	main()
