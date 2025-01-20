# tests/test_plot_utils.py

import pytest
import pandas as pd
from app.visualizations.plot_utils import generate_plots

@pytest.fixture
def sample_data():
    """Provide sample data for testing."""
    return pd.DataFrame({
        'track_genre': ['pop', 'rock', 'jazz', 'pop', 'rock'],
        'popularity': [80, 70, 60, 90, 85],
        'energy': [0.8, 0.7, 0.6, 0.9, 0.85],
        'tempo': [120, 110, 100, 130, 125],
        'danceability': [0.7, 0.6, 0.5, 0.8, 0.75],
        'duration_ms': [200000, 180000, 220000, 210000, 190000],
        'valence': [0.6, 0.5, 0.4, 0.7, 0.65]
    })

def test_generate_plots(tmpdir, sample_data):
    """Test that generate_plots returns a list of dictionaries with encoded images."""
    # Save sample data to a temporary CSV file
    data_file = tmpdir.join("test_data.csv")
    sample_data.to_csv(data_file, index=False)

    # Call the function
    plots = generate_plots(data_file)

    # Verify the output
    assert isinstance(plots, list)
    assert len(plots) == 5  # 5 plots are generated

    for plot in plots:
        assert 'title' in plot
        assert 'image' in plot
        assert 'interpretation' in plot
        assert plot['image'].startswith('data:image/png;base64')  # Verify the image is base64 encoded