#!/usr/bin/env python3

import sys  # Import the sys module for command line arguments
import csv  # Import the csv module for writing to CSV files
from postal.parser import parse_address  # Import the parse_address function from the postal.parser module

def parse_address_file(input_file, output_file):
    parsed_addresses = []  # Create an empty list to store parsed addresses
    with open(input_file, 'r') as f:  # Open the input file in read mode
        for address in f:  # Loop over each address in the file
            address = address.strip()  # Remove leading/trailing whitespace and newlines
            components = parse_address(address)  # Parse the address components
            parsed_addresses.append(components)  # Append the parsed components to the list

    with open(output_file, 'w') as f:  # Open the output file in write mode
        writer = csv.writer(f)  # Create a CSV writer object
        writer.writerows(parsed_addresses)  # Write the parsed addresses to the output file

# Check if the input and output file names are provided as command line arguments
if len(sys.argv) != 3:
    print("Usage: address_parser.py input_file output_file")
    sys.exit()

# Get the input and output file names from the command line arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# Parse the addresses in the input file and write the parsed data to the output file
parse_address_file(input_file, output_file)

