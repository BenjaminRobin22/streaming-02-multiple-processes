import csv
import socket
import time
import logging

logging.basicConfig(filename="out9.txt", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

HOST = "localhost"
PORT = 9999
ADDRESS = (HOST, PORT)
INPUT_FILE = "mlb-player-stats-p.csv"

def prepare_message(row):
    player, team, ip, era = row[0], row[1], row[7], row[18]
    return f"[{player}, {team}, {ip}, {era}]".encode()

def stream_data(input_file, address):
    with open(input_file, "r") as file:
        reader = csv.reader(file, delimiter="\t")
        next(reader)  # Skip header
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        for row in reader:
            message = prepare_message(row)
            sock.sendto(message, address)
            logging.info(f"Sent: {message} to {address}. Hit CTRL-c to stop.")
            time.sleep(3)

if __name__ == "__main__":
    try:
        logging.info("Starting fake streaming process.")
        stream_data(INPUT_FILE, ADDRESS)
        logging.info("Streaming complete!")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
