#!/usr/bin/env python3

import sys
import json
from postal.parser import parse_address

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

            # Extract the parsed components and store them as key-value pairs
            for component in components:
                if component[1]:
                    parsed_components[component[1]] = component[0]

            # Append the parsed components to the list
            parsed_addresses.append(parsed_components)

    # Write the parsed addresses to a JSON file
    with open(output_file, 'w') as f:
        json.dump(parsed_addresses, f)

# Check if the input and output file names are provided as command line arguments
if len(sys.argv) != 3:
    print("Usage: address_parser.py input_file output_file")
    sys.exit()

input_file = sys.argv[1]
output_file = sys.argv[2]

# Parse the addresses in the input file and write the parsed data to the output file
parse_address_file(input_file, output_file)

