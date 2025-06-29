from google.cloud import storage
import os   
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
BUCKET_NAME = "gmaps-change-detector"
SAVED_GCP_SCREENSHOT_NAME = "saved_gcp_screenshot.jpeg"

def upload_image_to_gcs(local_path):
    # Initialize client
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(SAVED_GCP_SCREENSHOT_NAME)

    # Upload file
    blob.upload_from_filename(local_path)
    print(f"Uploaded {local_path} to gs://{BUCKET_NAME}/{SAVED_GCP_SCREENSHOT_NAME}")

def download_image_from_gcs(local_path):
    # Initialize client
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(SAVED_GCP_SCREENSHOT_NAME)

    # Download file
    blob.download_to_filename(local_path)
    print(f"Downloaded {SAVED_GCP_SCREENSHOT_NAME} from gs://{BUCKET_NAME} to {local_path}")

def delete_image_from_gcs():
    # Initialize client
    storage_client = storage.Client()
    bucket = storage_client.bucket(BUCKET_NAME)
    blob = bucket.blob(SAVED_GCP_SCREENSHOT_NAME)

    # Delete file
    blob.delete()
    print(f"Deleted {SAVED_GCP_SCREENSHOT_NAME} from gs://{BUCKET_NAME}")

def image_exists():
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(SAVED_GCP_SCREENSHOT_NAME)
    return blob.exists()