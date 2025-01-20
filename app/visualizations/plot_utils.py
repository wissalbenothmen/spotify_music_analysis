import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

def generate_plots(data_file):
    """Generates plots for the dashboard."""
    df = pd.read_csv(data_file)

    plots = []

    # Plot 1: Genre Popularity
    plt.figure(figsize=(10, 6))
    genre_popularity = df.groupby('track_genre')['popularity'].mean().sort_values(ascending=False).head(10)
    sns.barplot(x=genre_popularity.values, y=genre_popularity.index)
    plt.title('Top 10 Genres by Average Popularity')
    plt.xlabel('Average Popularity')
    plt.ylabel('Genre')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.read()).decode('utf8')
    plots.append({
        'title': 'Top 10 Genres by Average Popularity',
        'image': f'data:image/png;base64,{plot_url}',
        'interpretation': 'This plot shows the top 10 genres by average popularity.'
    })

    # Plot 2: Energy vs Tempo by Genre
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='energy', y='tempo', hue='track_genre', data=df, palette='viridis')
    plt.title('Energy vs Tempo by Genre')
    plt.xlabel('Energy')
    plt.ylabel('Tempo')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.read()).decode('utf8')
    plots.append({
        'title': 'Energy vs Tempo by Genre',
        'image': f'data:image/png;base64,{plot_url}',
        'interpretation': 'This plot shows the relationship between energy and tempo for different genres.'
    })

    # Plot 3: Danceability Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(df['danceability'], bins=30, kde=True)
    plt.title('Danceability Distribution')
    plt.xlabel('Danceability')
    plt.ylabel('Frequency')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.read()).decode('utf8')
    plots.append({
        'title': 'Danceability Distribution',
        'image': f'data:image/png;base64,{plot_url}',
        'interpretation': 'This plot shows the distribution of danceability across all tracks.'
    })

    # Plot 4: Popularity vs Duration
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='popularity', y='duration_ms', data=df)
    plt.title('Popularity vs Duration')
    plt.xlabel('Popularity')
    plt.ylabel('Duration (ms)')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.read()).decode('utf8')
    plots.append({
        'title': 'Popularity vs Duration',
        'image': f'data:image/png;base64,{plot_url}',
        'interpretation': 'This plot shows the relationship between popularity and duration.'
    })

    # Plot 5: Valence vs Energy
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='valence', y='energy', data=df)
    plt.title('Valence vs Energy')
    plt.xlabel('Valence')
    plt.ylabel('Energy')
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plot_url = base64.b64encode(buf.read()).decode('utf8')
    plots.append({
        'title': 'Valence vs Energy',
        'image': f'data:image/png;base64,{plot_url}',
        'interpretation': 'This plot shows the relationship between valence and energy.'
    })

    return plots