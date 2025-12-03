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

if __name__ == "__main__":
    # This block runs when the script is executed directly
    print("--- Running visualizer.py module example ---")

    # 1. Create a sample DataFrame
    sample_hurricane_data = {
        'state': ['Florida', 'Texas', 'Louisiana', 'Florida', 'Texas', 'Florida'],
        'damage_usd': [1000, 3500, 1200, 2000, 4000, 500]
    }
    df_sample = pd.DataFrame(sample_hurricane_data)

    print("\nSample Data:")
    print(df_sample)

    # 2. Use the create_pie_chart function to generate an example plot
    print("\nGenerating example pie chart...")
    create_pie_chart(df_sample, 'state',
                     title='Example: Hurricane Landfalls by State',
                     output_path='main_pie_chart.png')

    print("\n--- Example finished ---")
