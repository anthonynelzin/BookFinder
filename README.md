# BookFinder

BookFinder is a set of Python scripts that help maintain [my personal reading log](https://metrozendodo.fr/biblio/ 'Biblio | métro[zen]dodo'). BookFinder validates the supplied ISBN-10 or ISBN-13, searches for the corresponding book on the [Open Library](https://openlibrary.org/ 'Welcome to Open Library | Open Library'), downloads the cover, and creates a log file ready for the Hugo static site generator. As a whole, BookFinder shouldn’t be of any use to you. But if you need to validate ISBNs, to learn how to use the Open Library API, or to fake knowing as little Python as I do, have fun hacking away at it!

## Usage

	python3 bookfinder.py [-h] --isbn ISBN --slug SLUG
	
- `ISBN`: a valid ISBN-10 or ISBN-13
- `SLUG`: the reading log slug

## Requirements

None.

## Licence

EUPL 1.2.