#!/usr/bin/env python3

import sys
import requests 
import json
from postal.parser import parse_address

api_key = sys.argv[1]

def get_geocode(address):
    # Google Maps Geocoding API endpoint
    endpoint = 'https://maps.googleapis.com/maps/api/geocode/json'

    # Parameters for the API request
    params = {
        'address': address,
        'key': api_key
    }

    # Send the API request
    response = requests.get(endpoint, params=params)

    # Parse the response JSON
    response_json = json.loads(response.text)

    # Extract the latitude and longitude from the response
    if response_json['status'] == 'OK':
        lat = response_json['results'][0]['geometry']['location']['lat']
        lng = response_json['results'][0]['geometry']['location']['lng']
        return lat, lng
    else:
        print(response_json)
        return None, None

def parse_address_file(input_file, output_file):
    parsed_addresses = []
    with open(input_file, 'r') as f:
        for address in f:
            # Remove leading/trailing whitespace and newlines
            address = address.strip()

            # Parse the address components
            components = parse_address(address)

            # Create a dictionary to store the parsed components
            parsed_components = {}

            # Get the latitude and longitude for the address
            lat, lng = get_geocode(address)

            # Extract the parsed components and store them as key-value pairs
            for component in components:
                if component[1]:
                    parsed_components[component[1]] = component[0]
            
            parsed_components['address'] = address 
            parsed_components['lat'] = lat
            parsed_components['lng'] = lng

            # Append the parsed components to the list
            parsed_addresses.append(parsed_components)

    # Write the parsed addresses to a JSON file
    with open(output_file, 'w') as f:
        json.dump(parsed_addresses, f)

# Check if the input and output file names are provided as command line arguments
if len(sys.argv) != 3:
    print("Usage: address_parser.py input_file output_file")
    sys.exit()


input_file = sys.argv[2]
output_file = sys.argv[3]

# Parse the addresses in the input file and write the parsed data to the output file
parse_address_file(input_file, output_file)

