
# Spotify Music Analysis - Flask Application

This is a Flask web application for analyzing Spotify music data. It provides visualizations and insights into a dataset of Spotify tracks, including genre popularity, energy vs. tempo, danceability distribution, and more.

## Project Structure

```plaintext
spotify_music_analysis/
├── app/                             # Dossier principal de l'application
│   ├── __init__.py                  # Fonction d'usine pour initialiser l'application Flask
│   ├── routes.py                    # Définition des routes de l'application
│   ├── templates/                   # Modèles HTML pour le rendu des pages
│   │   ├── base.html                # Layout de base pour toutes les pages
│   │   ├── index.html               # Page d'accueil
│   │   ├── dashboard.html           # Page avec les visualisations
│   │   ├── data.html                # Page affichant les données brutes
│   ├── static/                      # Ressources statiques (CSS, JS, images)
│   │   ├── style.css                # Feuille de style CSS
│   │   ├── script.js                # Fichier JavaScript (interactions éventuelles)
│   ├── utils/                       # Modules utilitaires pour réutiliser du code
│   │   ├── data_loader.py           # Fonctions pour télécharger et charger les données
│   ├── visualizations/              # Logique liée aux visualisations
│       ├── plot_utils.py            # Génération des graphiques
│
├── data/                            # Dossier pour les datasets téléchargés
│   ├── spotify_tracks.csv           # Dataset Spotify (téléchargé automatiquement)
│
├── tests/                           # Tests unitaires pour le projet
│   ├── __init__.py                  # Marque le dossier comme un package
│   ├── test_data_loader.py          # Tests pour les fonctions de chargement de données
│   ├── test_plot_utils.py           # Tests pour les fonctions de visualisation
│
├── poetry.lock                      # Fichier de verrouillage des dépendances Poetry
├── pyproject.toml                   # Configuration Poetry pour le projet
├── README.md                        # Documentation du projet
└── run.py                           # Point d'entrée pour exécuter l'application Flask

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
