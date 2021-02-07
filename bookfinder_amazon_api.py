#!/usr/bin/env python3

"""
	Anthony Nelzin-Santos
	anthony@nelzin.fr
	https://anthony.nelzin.fr

	European Union Public License 1.2
"""

from paapi5_python_sdk.api.default_api import DefaultApi
from paapi5_python_sdk.search_items_request import SearchItemsRequest
from paapi5_python_sdk.search_items_resource import SearchItemsResource
from paapi5_python_sdk.partner_type import PartnerType
from paapi5_python_sdk.rest import ApiException

def search_items(isbn, access, secret, host, region, tag):
	# Setup API
	default_api = DefaultApi(
		access_key = access,
		secret_key = secret,
		host = host,
		region = region
	)

	# Setup search
	partner_tag = tag
	item_count = 1
	keywords = isbn

	# Setup resources from SearchItemsResource
	search_items_resource = [
		SearchItemsResource.IMAGES_PRIMARY_LARGE,
		SearchItemsResource.ITEMINFO_BYLINEINFO,
		SearchItemsResource.ITEMINFO_CONTENTINFO,
		SearchItemsResource.ITEMINFO_EXTERNALIDS,
		SearchItemsResource.ITEMINFO_FEATURES,
		SearchItemsResource.ITEMINFO_MANUFACTUREINFO,
		SearchItemsResource.ITEMINFO_PRODUCTINFO,
		SearchItemsResource.ITEMINFO_TECHNICALINFO,
		SearchItemsResource.ITEMINFO_TITLE,
		SearchItemsResource.ITEMINFO_TRADEININFO,
	]

	# Request
	try:
		search_items_request = SearchItemsRequest(
			partner_tag = partner_tag,
			partner_type = PartnerType.ASSOCIATES,
			keywords = keywords,
			item_count = item_count,
			resources = search_items_resource,
		)
	except ValueError as exception:
		print("Error in forming SearchItemsRequest: ", exception)
		return

	try:
		response = default_api.search_items(search_items_request)
		
		if response.search_result is not None:
			print("Amazon API called successfully.")
			item = response.search_result.items[0]
			if item is not None:
				print("The book was found on Amazon. Its ASIN is: " + item.asin + ".")
			return item
				
	except ApiException as exception:
		print("Error calling PA-API 5.0!")
		print("Status code:", exception.status)
		print("Errors :", exception.body)
		print("Request ID:", exception.headers["x-amzn-RequestId"])

	except TypeError as exception:
		print("TypeError :", exception)

	except ValueError as exception:
		print("ValueError :", exception)

	except Exception as exception:
		print("Exception :", exception)
		
def main():
	search_items(isbn, access, secret, host, region, tag)
	
if __name__ == '__main__':
	main()