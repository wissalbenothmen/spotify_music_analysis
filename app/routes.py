from flask import Blueprint, render_template
from .utils.data_loader import download_data, load_data
from .visualizations.plot_utils import generate_plots
import pandas as pd

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/dashboard')
def dashboard():
    data_file = download_data()
    if data_file:
        df = pd.read_csv(data_file)
        total_tracks = len(df)
        avg_popularity = df['popularity'].mean()
        avg_duration = df['duration_ms'].mean()
        plots = generate_plots(data_file)
        return render_template('dashboard.html', plots=plots, total_tracks=total_tracks, avg_popularity=avg_popularity, avg_duration=avg_duration)
    return render_template('dashboard.html', plots=None)

@main.route('/data')
def data():
    df = load_data()
    if df is not None:
        data = df.to_dict(orient='records')
        return render_template('data.html', data=data)
    return render_template('data.html', data=[])