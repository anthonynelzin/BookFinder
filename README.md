# BookFinder

BookFinder is a set of Python scripts that help maintain [my personal reading log](https://metrozendodo.fr/biblio/ 'Biblio | métro[zen]dodo'). BookFinder validates the supplied ISBN-10 or ISBN-13, searches for the corresponding book on Amazon using the [Product Advertising API 5.0](https://webservices.amazon.com/paapi5/documentation/ 'Introduction · Product Advertising API 5.0'), downloads the cover, and creates a log file ready for the Hugo static site generator. As a whole, BookFinder shouldn’t be of any use to you. But if you need to validate ISBNs, to learn how to use the official PA-API module, or to fake knowing as little Python as I do, have fun hacking away at it!

## Usage

	python3 bookfinder.py
	
BookFinder will ask you to input an ISBN-10 or ISBN-13. If you supply a valid ISBN, BookFinder will proceed.

## Requirements

- some PA-API keys
- python-amazon-paapi

## Licence

EUPL 1.2.