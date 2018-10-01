def parser(json):
    address_list = {}
    if json['results']:
        data = json['results'][0]
        for item in data['address_components']:
            for category in item['types']:
                data[category] = {}
                data[category] = item['long_name']
        address_list['street'] = data.get("route", None)
        address_list['state'] = data.get("administrative_area_level_1", None)
        address_list['city'] = data.get("locality", None)
        address_list['county'] = data.get("administrative_area_level_2", None)
        address_list['country'] = data.get("country", None)
        address_list['postal_code'] = data.get("postal_code", None)
        address_list['neighborhood'] = data.get("neighborhood",None)
        address_list['sublocality'] = data.get("sublocality", None)
        address_list['housenumber'] = data.get("housenumber", None)
        address_list['postal_town'] = data.get("postal_town", None)
        address_list['subpremise'] = data.get("subpremise", None)
        address_list['latitude'] = data.get("geometry", {}).get("location", {}).get("lat", None)
        address_list['longitude'] = data.get("geometry", {}).get("location", {}).get("lng", None)
        address_list['location_type'] = data.get("geometry", {}).get("location_type", None)
        address_list['postal_code_suffix'] = data.get("postal_code_suffix", None)
        address_list['street_number'] = data.get('street_number', None)
    return address_list
