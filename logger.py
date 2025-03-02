import logging
import os

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Configure logging
logging.basicConfig(
    filename="logs/qr_scanner.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def log_qr_scan(data):
    """
    Logs scanned QR code data.
    """
    logging.info(f"Scanned QR Code: {data}")

def log_qr_generation(content):
    """
    Logs generated QR code content.
    """
    logging.info(f"Generated QR Code Content: {content}")

def log_error(error_message):
    """
    Logs errors occurring in QR generation or scanning.
    """
    logging.error(f"Error: {error_message}")