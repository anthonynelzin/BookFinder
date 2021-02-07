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
# https://webservices.amazon.fr/paapi5/scratchpad/index.html

from bookfinder_isbn_check import *
from bookfinder_amazon_api import *
from datetime import datetime
import argparse
import string
import unicodedata
import urllib.request

def reading_notes_generator(isbn, item):
	print("Creating reading log…")

	book_title = item.item_info.title.display_value
	print("Title: " + book_title)
	
	if item.item_info.by_line_info.contributors:
		# Should be refactored with iteration to get multiple authors
		# but Amazon's way of storing that info isn't that great.
		book_author = item.item_info.by_line_info.contributors[0].name
		print("Author: " + book_author)
		
	if item.item_info.by_line_info.manufacturer:
		book_publisher = item.item_info.by_line_info.manufacturer.display_value
		print("Publisher: " + book_publisher)
	
	if item.item_info.product_info.release_date:
		book_date = item.item_info.product_info.release_date.display_value[:4]
		print("Year: " + book_date)
	
	if item.item_info.content_info.pages_count:
		book_pages = str(item.item_info.content_info.pages_count.display_value)
		print("# of pages: " + book_pages)
		
	book_isbn = isbn_clean(isbn)
	
	if item.images.primary.large:
		book_image = item.images.primary.large.url
		print("Cover: " + book_image)
	
	book_url = item.detail_page_url
	print("URL: " + book_url)

	cruft = "',;:=?./+-_&()!@#<>"
	uncruft = str.maketrans("", "", cruft)
	author_name = unicodedata.normalize('NFKD', book_author.translate(
		uncruft).split()[1].lower()).encode('ascii', 'ignore').decode("utf-8")
	book_id = unicodedata.normalize('NFKD', book_title.translate(uncruft).split()[
								   0].lower()).encode('ascii', 'ignore').decode("utf-8")
	book_slug = author_name + "-" + book_id

	# Let's do this
	file = open("index.md", "w")
	file.write("---\n")
	file.write("title: \"" + book_title + "\"\n")
	file.write(
		"publishDate: " + datetime.now().strftime("%Y-%m-%dT%H:%M:%S" + "+01:00") + "\n")
	file.write(
		"date: " + datetime.now().strftime("%Y-%m-%dT%H:%M:%S" + "+01:00") + "\n")
	file.write("biblio_auteurs: \n")
	if book_author:
		file.write("- \"" + book_author + "\"\n")
	if book_publisher:
		file.write("biblio_editeurs: \n- \"" + book_publisher + "\"\n")
	if book_date:
		file.write("annee: " + book_date + "\n")
	if book_pages:
		file.write("pages: " + book_pages + "\n")
	file.write("isbn: " + isbn + "\n")
	file.write("biblio_localisations: \n- \"\"\n")
	file.write("achatDate: \"\"\n")
	file.write("achatLieu: \"\"\n")
	file.write("achatPrix: \"\"\n")
	file.write("lecture: \n- \"\"\n")
	file.write("link: \n")
	file.write("- \"<a href='" + book_url + "'>Amazon</a>\"\n")
	file.write("- \"<a href='https://www.decitre.fr/livres/" + book_isbn + ".html'>Decitre</a>\"\n")
	file.write("- \"<a href='https://www.leslibraires.fr/livre/" + book_isbn + "'>Les libraires</a>\"\n")
	file.write("- \"<a href='https://www.placedeslibraires.fr/livre/" + book_isbn + "'>Place des libraires</a>\"\n")
	file.write("layout: single-biblio\n")
	file.write("slug: " + book_slug + "\n")
	file.write("biblio_tags: \n- \"\"\n")
	file.write("---\n\n")
	file.write("## Notes\n\n## Notes archivistiques\n\n")
	
	file.close()

	if book_image:
		urllib.request.urlretrieve("" + book_image, "hero.jpg")

	print("Your reading log is ready.")
		
def main():
	parser = argparse.ArgumentParser(description="A needlessly complicated way to maintain my reading log.")
	parser.add_argument("-i", "--isbn", help="An ISBN-10 or ISBN-13.")
	parser.add_argument("-a", "--access", help="Your Amazon PA-API access key.")
	parser.add_argument("-s", "--secret", help="Your Amazon PA-API secret key.")
	parser.add_argument("-x", "--host", default="webservices.amazon.fr", help="Your Amazon host.")
	parser.add_argument("-r", "--region", default="eu-west-1", help="Your Amazon region.")
	parser.add_argument("-t", "--tag", default="mzd-21", help="Your Amazon associate tag.")
	
	args = parser.parse_args()
	
	isbn = args.isbn
	access = args.access
	secret = args.secret
	host = args.host
	region = args.region
	tag = args.tag

	isbn_check(isbn)
	item = search_items(isbn, access, secret, host, region, tag)
	reading_notes_generator(isbn, item)
	
if __name__ == '__main__':
	main()