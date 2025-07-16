import detector
import time

if __name__ == "__main__":
    while True:
        detector.detect_change()
        time.sleep(24 * 60 * 60) # sleep for 24 hours