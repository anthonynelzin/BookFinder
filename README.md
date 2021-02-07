# BookFinder

BookFinder is a set of Python scripts that help maintain [my personal reading log](https://metrozendodo.fr/biblio/ 'Biblio | métro[zen]dodo'). BookFinder validates the supplied ISBN-10 or ISBN-13, searches for the corresponding book on Amazon using the [Product Advertising API 5.0](https://webservices.amazon.com/paapi5/documentation/ 'Introduction · Product Advertising API 5.0'), downloads the cover, and creates a log file ready for the Hugo static site generator. As a whole, BookFinder shouldn’t be of any use to you. But if you need to validate ISBNs, to learn how to use the official PA-API module, or to fake knowing as little Python as I do, have fun hacking away at it!

## Usage

	python3 bookfinder.py [-h] --isbn ISBN --access ACCESS --secret SECRET [--host HOST] [--region REGION] [--tag TAG]
	
- `ISBN`: a valid ISBN-10 or ISBN-13
- `ACCESS`: your Amazon PA-API access key
- `SECRET`: your Amazon PA-API secret key
- `HOST`: your Amazon host (default: `webservices.amazon.fr`)
- `REGION`: your Amazon region (default: `eu-west-1`)
- `TAG`: your Amazon associate tag (default: `mzd-21`)

## Requirements

- some PA-API keys
- python-amazon-paapi

## Licence

EUPL 1.2.