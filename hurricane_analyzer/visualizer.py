import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium

def load_data(filepath):
    """Loads data from a CSV file."""
    return pd.read_csv(filepath)

def create_pie_chart(data, column, title='Pie Chart', output_path='pie_chart.png'):
    """Generates a pie chart for a given column and saves it to a file."""
    plt.figure(figsize=(8, 8))
    data[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
    plt.title(title)
    plt.ylabel('')  # Hide the y-label
    plt.savefig(output_path)
    plt.close()

def create_bar_graph(data, x_column, y_column):
    """Generates a bar graph."""
    pass

def create_map_plot(data, lat_column, lon_column, popup_column):
    """Generates a map plot."""
    pass
