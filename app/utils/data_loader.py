import pandas as pd
import requests
import os

DATASET_URL = "https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/resolve/main/dataset.csv"
DATA_FILE = "data/spotify_tracks.csv"

def download_data():
    """Downloads the dataset if it doesn't exist."""
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(DATA_FILE):
        print("Downloading dataset...")
        try:
            response = requests.get(DATASET_URL, stream=True)
            response.raise_for_status()  # Raise an exception for bad status codes

            with open(DATA_FILE, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print("Download complete.")
        except requests.exceptions.RequestException as e:
            print(f"Error during download: {e}")
            return None
    else:
        print("Dataset already exists.")
    return DATA_FILE

def load_data():
    """Loads the dataset and returns it as a DataFrame."""
    data_file = download_data()
    if data_file:
        return pd.read_csv(data_file)
    return None
