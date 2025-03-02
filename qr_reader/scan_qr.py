import pygame
import numpy as np
import cv2
from pyzbar.pyzbar import decode
from PIL import ImageGrab
import textwrap
import time
from logger import log_qr_scan, log_error

def capture_screen():
    """
    Continuously captures the screen until a QR code is detected.
    """
    print("Waiting for QR code to appear on the screen...")
    while True:
        time.sleep(1)  # Capture screen every second
        try:
            screenshot = ImageGrab.grab()  # Capture the full screen
            qr_data = decode_qr_from_image(screenshot)
            if qr_data:
                return screenshot, qr_data  # Return both image and QR data
        except Exception as e:
            log_error(f"Error capturing screen: {e}")
            return None, None

def decode_qr_from_image(image):
    """
    Decodes QR codes from a given image.
    """
    try:
        gray_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2GRAY)  # Convert to grayscale
        decoded_objects = decode(gray_image)

        if decoded_objects:
            qr_data = decoded_objects[0].data.decode("utf-8")  # Return first detected QR code
            log_qr_scan(qr_data)
            return qr_data
        return None  # Return None if no QR found
    except Exception as e:
        log_error(f"Error decoding QR: {e}")
        return None

def display_result(qr_data):
    """
    Displays the scanned QR code data in a pygame window with text auto-wrapping.
    """
    pygame.init()
    
    screen_width = 700
    padding = 20
    font_size = 32
    font = pygame.font.Font(None, font_size)

    wrapped_text = textwrap.wrap(qr_data, width=50)
    text_surfaces = [font.render(line, True, (0, 0, 0)) for line in wrapped_text]

    line_height = font_size + 10
    window_height = padding * 2 + len(text_surfaces) * line_height
    screen = pygame.display.set_mode((screen_width, window_height))
    pygame.display.set_caption("QR Code Result")

    running = True
    while running:
        screen.fill((255, 255, 255))  # White background

        y_offset = padding
        for text_surface in text_surfaces:
            screen.blit(text_surface, (padding, y_offset))
            y_offset += line_height

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        pygame.display.flip()

    pygame.quit()

def main():
    """
    Main function to capture screen and scan for QR codes.
    """
    qr_image, qr_data = capture_screen()

    if qr_image and qr_data:
        print(f"Scanned QR Code Data: {qr_data}")
        display_result(qr_data)
    else:
        print("Failed to detect a QR code.")

if __name__ == "__main__":
    main()