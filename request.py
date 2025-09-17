import os
import requests
from urllib.parse import urlparse
import uuid

def fetch_image():
    print("🌍 The Wisdom of Ubuntu: 'I am because we are'")
    url = input("Please enter the URL of the image you want to fetch: ").strip()

    # Directory for fetched images
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Attempt to fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad responses (4xx/5xx)

        # Extract filename from URL or generate one
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        if not filename:  # If no filename in URL, generate one
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full path
        filepath = os.path.join(save_dir, filename)

        # Save the image in binary mode
        with open(filepath, "wb") as f:
            f.write(response.content)

        print(f"✅ Image fetched successfully and saved as: {filepath}")

    except requests.exceptions.MissingSchema:
        print("❌ Invalid URL. Please ensure you entered a proper link (e.g., https://example.com/image.jpg).")
    except requests.exceptions.HTTPError as http_err:
        print(f"❌ HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error. Please check your internet connection or the website’s availability.")
    except requests.exceptions.Timeout:
        print("❌ Request timed out. The server took too long to respond.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    fetch_image()
