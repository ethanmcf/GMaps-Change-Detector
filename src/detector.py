import email_handler
import os
import gc_handler
import gmaps_handler
from PIL import Image, ImageChops
import numpy as np  

def detect_change():
    """Assumes there is a saved gcp screenshot in the gcp bucket"""
    
    if not os.path.exists('src/screenshots/saved_gcp_screenshot.jpeg'):
        print("No local saved gcp screenshot found, downloading new one...")
        gc_handler.download_image_from_gcs('src/screenshots/saved_gcp_screenshot.jpeg')
    
    gmaps_handler.save_gmaps_image()

    new_screenshot = Image.open('src/screenshots/new_gmaps_screenshot.jpeg')
    saved_screenshot = Image.open('src/screenshots/saved_gcp_screenshot.jpeg')

    # Compare the blurred images
    diff = ImageChops.difference(saved_screenshot, new_screenshot)
    diff_np = np.array(diff)
    
    # Calculate how many pixels are different (non-zero)
    num_diff_pixels = np.count_nonzero(diff_np)
    total_pixels = diff_np.shape[0] * diff_np.shape[1] * diff_np.shape[2]
    diff_ratio = num_diff_pixels / total_pixels

    print(f"Verifying difference: {diff_ratio:.6f} ({diff_ratio * 100:.2f}%)")

    if diff_ratio > 0.1:
        print("Over 10 percent change detected ... sending email")
        email_handler.send_email()
    else:
        print("No change detected")


if __name__ == "__main__":
    detect_change()