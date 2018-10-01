# Imports
from csv import DictReader
from get_address import get_address_components

# User Values: Change The Values Below
# Place your Google Maps Geocoding API_KEY below
API_KEY = 'YOUR_API_KEY_HERE!!'

# language - The language in which to return results. Represented in two character language code.
# For the list of supported languages see here: https://developers.google.com/maps/faq#languagesupport
LANGUAGE = 'en'

# Region - The region code, specified as a ccTLD ("top-level domain") two-character value.
# This parameter will only influence, not fully restrict, results from the geocoder.
# See here: https://developers.google.com/maps/documentation/geocoding/intro#RegionCodes
REGION = 'nl'



if __name__ == '__main__':
    result_list = []
    with open("input.csv") as sourcefile:
        # Delimiter is set to newline character. Change the delimiter below if your CSV uses a different delimiter.
        addresses = DictReader(sourcefile, delimiter='\n')
        for i in addresses:
            for key, value in i.items():
                get_address_components(value, result_list, LANGUAGE, REGION, API_KEY,)
