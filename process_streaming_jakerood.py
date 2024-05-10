# Import from Python Standard Library

import csv
import socket
import time
import logging

# Set up basic configuration for logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# Declare program constants (typically constants are named with ALL_CAPS)

HOST = "localhost"
PORT = 9999
ADDRESS_TUPLE = (HOST, PORT)
INPUT_FILE_NAME = "MSFT_Hourly.csv"
OUTPUT_FILE_NAME = "out9.txt"

# Define program functions (bits of reusable code)

def prepare_message_from_row(row):
    """Prepare a binary message from a given row."""
    datetime, open_price, high, low, close, volume = row
    # use an fstring to create a message from our data
    # notice the f before the opening quote for our string?
    fstring_message = f"[{datetime}, {open_price}, {high}, {low}, {close}, {volume}]"

    # prepare a binary (1s and 0s) message to stream
    MESSAGE = fstring_message.encode()
    logging.debug(f"Prepared message: {fstring_message}")
    return MESSAGE


def stream_row(input_file_name, output_file_name, address_tuple):
    """Read from input file and stream data."""
    logging.info(f"Starting to stream data from {input_file_name} to {address_tuple}.")

    # Create a file object for input (r = read access)
    with open(input_file_name, "r") as input_file:
        logging.info(f"Opened for reading: {input_file_name}.")

        # Create a CSV reader object
        reader = csv.reader(input_file, delimiter=",")
        
        header = next(reader)  # Skip header row
        logging.info(f"Skipped header row: {header}")

        # use socket enumerated types to configure our socket object
        # Set our address family to (IPV4) for 'internet'
        # Set our socket type to UDP (datagram)
        ADDRESS_FAMILY = socket.AF_INET 
        SOCKET_TYPE = socket.SOCK_DGRAM 

        # Call the socket constructor, socket.socket()
        # A constructor is a special method with the same name as the class
        # Use the constructor to make a socket object
        # and assign it to a variable named `sock_object`
        sock_object = socket.socket(ADDRESS_FAMILY, SOCKET_TYPE)
        
        # Open the output file for writing
        with open(output_file_name, "w") as output_file:
            logging.info(f"Opened for writing: {output_file_name}.")

            # Write header to the output file
            output_file.write(",".join(header) + "\n")

            # Read rows
            for row in reader:
                message = prepare_message_from_row(row)
                # Stream via socket and write to output file
                sock_object.sendto(message, address_tuple)
                output_file.write(message.decode() + "\n") # Decode bytes to string before writing
                logging.info(f"Sent: {message} on port {PORT}. Wrote to {output_file_name}. Hit CTRL-c to stop.")
                time.sleep(3) # wait 3 seconds between writing rows

# ---------------------------------------------------------------------------
# If this is the script we are running, then call some functions and execute code!
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting custom streaming and writing process.")
        stream_row(INPUT_FILE_NAME, OUTPUT_FILE_NAME, ADDRESS_TUPLE)
        logging.info("Streaming and writing complete!")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

# Modified by Jake Rood on 05/10/2024