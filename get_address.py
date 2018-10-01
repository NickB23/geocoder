# Imports
from requests import get
from parser import parser
from write_data import write_data

def get_address_components(address, result_list, LANGUAGE, REGION, API_KEY,):
    url = 'https://maps.googleapis.com/maps/api/geocode/json?components=&language=' + LANGUAGE + '&region=' + REGION + '&bounds=&key=' + API_KEY
    url = url + '&address='+ address.replace(" ","+")
    response = get(url)
    parsed_data = parser(response.json())
    parsed_data['address'] = address
    result_list.append(parsed_data)
    # print(parsed_data)
    write_data(result_list)
