Here’s a **well-documented `README.md`** for your Flask application. It includes step-by-step instructions for setting up the project, running it, and understanding its structure. You can copy and paste this into your `README.md` file.

---

```markdown
# Spotify Music Analysis - Flask Application

This is a Flask web application for analyzing Spotify music data. It provides visualizations and insights into a dataset of Spotify tracks, including genre popularity, energy vs. tempo, danceability distribution, and more.

## Project Structure

```
spotify_music_analysis/
│
├── app/                             # Main application folder
│   ├── __init__.py                  # App factory function
│   ├── routes.py                    # Defines app routes
│   ├── templates/                   # HTML templates for rendering views
│   │   ├── base.html                # Base layout for all pages
│   │   ├── index.html               # Home page
│   │   ├── dashboard.html           # Dashboard page for visualizations
│   │   ├── data.html                # Data page to display raw data
│   ├── static/                      # Static assets (CSS, JS, images)
│   │   ├── style.css                # Stylesheet for the app
│   │   ├── script.js                # JavaScript (if needed for interaction)
│   ├── utils/                       # Utility modules for reusable code
│       ├── data_loader.py           # Functions for downloading/loading data
│   ├── visualizations/              # Subfolder for visualization logic
│       ├── plot_utils.py            # Generates visualizations
│
├── data/                            # Folder to store downloaded datasets
│   ├── spotify_tracks.csv           # Spotify dataset (downloaded automatically)
│
├── tests/                           # Folder for test cases
│   ├── __init__.py                  # Marks the folder as a package
│   ├── test_data_loader.py          # Tests for data loading functions
│   ├── test_plot_utils.py           # Tests for visualization functions
│
├── poetry.lock                      # Poetry lockfile for dependencies
├── pyproject.toml                   # Poetry configuration for the project
├── README.md                        # Project documentation
└── run.py                           # Entry point to run the Flask app
```

---

## Features

1. **Data Loading**:
   - Automatically downloads the Spotify dataset from Hugging Face.
   - Loads the dataset into a Pandas DataFrame for analysis.

2. **Visualizations**:
   - Generates interactive visualizations using Matplotlib and Seaborn.
   - Visualizations include:
     - Top 10 Genres by Average Popularity
     - Energy vs. Tempo by Genre
     - Danceability Distribution
     - Popularity vs. Duration
     - Valence vs. Energy

3. **Web Interface**:
   - Home page (`/`) with an introduction to the project.
   - Dashboard (`/dashboard`) to display visualizations and insights.
   - Data page (`/data`) to view the raw dataset.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.10 or higher**
- **Poetry** (for dependency management)
- **Git** (optional, for cloning the repository)

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/wissalbenothmen/spotify_music_analysis.git
cd spotify_music_analysis
```

### 2. Set Up a Virtual Environment

If you're using Poetry, it will handle the virtual environment for you. Otherwise, you can create one manually:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

Use Poetry to install the required dependencies:

```bash
poetry install
```

This will install all the dependencies listed in `pyproject.toml`.

---

## Running the Application

### 1. Start the Flask Development Server

Run the following command to start the Flask app:

```bash
poetry run python run.py
```

The app will be available at `http://127.0.0.1:5000`.

### 2. Access the Web Interface

- **Home Page**: `http://127.0.0.1:5000/`
- **Dashboard**: `http://127.0.0.1:5000/dashboard`
- **Data Page**: `http://127.0.0.1:5000/data`

---

## Testing

To run the tests, use the following command:

```bash
poetry run pytest tests/
```

This will execute all the test cases in the `tests/` folder.

---

## Key Files

### 1. `app/utils/data_loader.py`

- **`download_data()`**: Downloads the Spotify dataset if it doesn't already exist.
- **`load_data()`**: Loads the dataset into a Pandas DataFrame.

### 2. `app/visualizations/plot_utils.py`

- **`generate_plots()`**: Generates visualizations and returns them as base64-encoded images.

### 3. `app/routes.py`

- Defines the routes for the Flask app:
  - `/`: Home page.
  - `/dashboard`: Dashboard with visualizations.
  - `/data`: Page to display raw data.

### 4. `run.py`

- Entry point for the Flask application. Starts the development server.

---

## Customization

### Add New Visualizations

To add new visualizations, modify the `generate_plots()` function in `app/visualizations/plot_utils.py`. You can add new plots using Matplotlib or Seaborn.

### Modify Templates

The HTML templates are located in `app/templates/`. You can customize the layout, styles, and content as needed.

---

## Troubleshooting

### 1. Dataset Download Fails

If the dataset download fails, ensure you have an active internet connection. You can also manually download the dataset from [this link](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/resolve/main/dataset.csv) and place it in the `data/` folder.

### 2. Dependency Issues

If you encounter dependency issues, try reinstalling the dependencies:

```bash
poetry install --no-cache
```

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- Dataset: [Spotify Tracks Dataset](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset) by Maharshi Pandya.
- Libraries: Flask, Pandas, Matplotlib, Seaborn, Poetry.

---

Enjoy exploring the Spotify dataset with this Flask app! 🎵
```

---

### How to Use This README

1. Copy the entire content above into a file named `README.md` in the root of your project.
2. Replace `your-username` in the clone URL with your actual GitHub username (if applicable).
3. Customize the sections (e.g., Acknowledgments, License) as needed.

This README provides clear instructions for setting up, running, and understanding your Flask application. It’s designed to be user-friendly and comprehensive. Let me know if you need further assistance! 🚀