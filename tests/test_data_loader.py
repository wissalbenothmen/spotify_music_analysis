# tests/test_data_loader.py

import os
import pytest
import pandas as pd
from app.utils.data_loader import download_data, load_data

@pytest.fixture
def mock_requests_get(mocker):
    """Mock the requests.get function to avoid actual HTTP requests."""
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.iter_content.return_value = [b"mock,data,content"]
    mocker.patch("requests.get", return_value=mock_response)

def test_download_data_new_file(tmpdir, mock_requests_get):
    """Test downloading a new file."""
    # Change working directory to tmpdir
    os.chdir(tmpdir)

    # Call the function
    result = download_data()

    # Normalize paths for comparison
    expected_path = os.path.normpath("data/spotify_tracks.csv")
    result_path = os.path.normpath(result)

    # Verify the file was created and the path is correct
    assert os.path.exists(expected_path)
    assert result_path == expected_path

def test_download_data_existing_file(tmpdir):
    """Test that the function does not download if the file already exists."""
    # Change working directory to tmpdir
    os.chdir(tmpdir)

    # Create the data directory and file
    os.makedirs("data")
    data_file = os.path.join("data", "spotify_tracks.csv")
    with open(data_file, "w") as f:
        f.write("mock,data,content")

    # Call the function
    result = download_data()

    # Normalize paths for comparison
    expected_path = os.path.normpath(data_file)
    result_path = os.path.normpath(result)

    # Verify the function returns the correct path
    assert result_path == expected_path

def test_load_data(tmpdir, mock_requests_get):
    """Test that load_data returns a valid DataFrame."""
    # Change working directory to tmpdir
    os.chdir(tmpdir)

    # Create the data directory and file
    os.makedirs("data")
    data_file = os.path.join("data", "spotify_tracks.csv")
    with open(data_file, "w") as f:
        f.write("col1,col2\n1,2\n3,4")

    # Call the function
    df = load_data()

    # Verify the DataFrame is loaded correctly
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (2, 2)

def test_load_data_no_file(tmpdir, mocker):
    """Test that load_data returns None if the file does not exist."""
    # Change working directory to tmpdir
    os.chdir(tmpdir)

    # Ensure the data directory does not exist
    if os.path.exists("data"):
        os.rmdir("data")

    # Mock download_data to return None
    mocker.patch("app.utils.data_loader.download_data", return_value=None)

    # Call the function
    df = load_data()

    # Verify the function returns None
    assert df is None