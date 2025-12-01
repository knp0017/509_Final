import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium


def load_data(filepath):
    """Loads a pandas DataFrame from a CSV file.

    Args:
        filepath (str): The path to the CSV file.

    Returns:
        pandas.DataFrame: The loaded DataFrame, or None if an error occurs.
    """
    if not isinstance(filepath, str) or not os.path.exists(filepath):
        print(f"Error: Filepath '{filepath}' not found or is not a valid path.")
        return None
    try:
        df = pd.read_csv(filepath)
        return df
    except pd.errors.ParserError:
        print(f"Error: Could not parse '{filepath}'. Please ensure it is a valid CSV.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred while reading '{filepath}': {e}")
        return None

def create_pie_chart(data, column, title='Pie Chart', output_path='pie_chart.png'):
    """Generates a pie chart and saves it to a file.

    Args:
        data (pandas.DataFrame): The DataFrame containing the plot data.
        column (str): The column to visualize with the pie chart.
        title (str, optional): The title for the chart. Defaults to 'Pie Chart'.
        output_path (str, optional): The path to save the chart image.
                                     Defaults to 'pie_chart.png'.
    """
    # --- Input Validation ---
    if not isinstance(data, pd.DataFrame):
        print("Error: 'data' must be a pandas DataFrame.")
        return
    if not isinstance(column, str) or column not in data.columns:
        print(f"Error: Column '{column}' not found in the DataFrame.")
        return

    # --- Plotting Logic ---
    try:
        plt.figure(figsize=(8, 8))
        data[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90)
        plt.title(title)
        plt.ylabel('')  # Hide the y-label for a cleaner look

        plt.savefig(output_path)
        print(f"Pie chart saved successfully to '{output_path}'")
    except Exception as e:
        print(f"An error occurred while creating the pie chart: {e}")
    finally:
        plt.close()  # Free up memory

def create_bar_graph(data, x_column, y_column):
    """Generates a bar graph."""
    pass

def create_map_plot(data, lat_column, lon_column, popup_column):
    """Generates a map plot."""
    pass
