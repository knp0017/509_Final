# hurricane_analyzer/visualizer.py

import os
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import geopandas
from shapely.geometry import Point

def create_pie_chart(dataset, variable, title='Pie Chart', output_path='pie_chart.png'):
    """Generates a pie chart from a specified variable in an xarray Dataset."""
    # --- 1. Input Validation ---
    if not isinstance(dataset, xr.Dataset):
        print("Error: 'dataset' must be an xarray Dataset.")
        return
    if variable not in dataset.variables:
        print(f"Error: Variable '{variable}' not found in the Dataset.")
        return

    # --- 2. Plotting Logic ---
    try:
        # For categorical counts, converting to a pandas Series is the most direct way.
        data_series = dataset[variable].to_series()
        value_counts = data_series.value_counts()

        # Create the plot figure.
        plt.figure(figsize=(10, 10))

        # The main plotting call. autopct formats the percentage labels.
        plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)

        plt.title(title, fontsize=16, weight='bold')
        plt.ylabel('')  # Hiding the y-label makes pie charts cleaner.
        plt.axis('equal')  # Ensures the pie chart is a perfect circle.

        # --- 3. Save to File ---
        plt.savefig(output_path, bbox_inches='tight')
        print(f"Pie chart saved successfully to '{output_path}'")

    except Exception as e:
        print(f"An error occurred while creating the pie chart: {e}")
    finally:
        # It's crucial to close the plot to free up memory,
        # especially in a tool that might be run multiple times.
        plt.close()

def create_bar_graph(dataset, x_variable, y_variable, title='Bar Graph', output_path='bar_graph.png'):
    """Generates a bar graph from specified variables in an xarray Dataset."""
    # --- 1. Input Validation ---
    if not isinstance(dataset, xr.Dataset):
        print("Error: 'dataset' must be an xarray Dataset.")
        return
    if x_variable not in dataset.variables or y_variable not in dataset.variables:
        print(f"Error: One or both variables ('{x_variable}', '{y_variable}') not found.")
        return

    # --- 2. Plotting Logic ---
    try:
        # Seaborn works most elegantly with pandas DataFrames.
        df = dataset.to_dataframe().reset_index()

        plt.figure(figsize=(12, 7))
        sns.barplot(x=x_variable, y=y_variable, data=df, palette='viridis')

        plt.title(title, fontsize=16, weight='bold')
        plt.xlabel(x_variable, fontsize=12)
        plt.ylabel(y_variable, fontsize=12)
        plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability.
        plt.tight_layout()  # Adjust layout to prevent labels from overlapping.

        # --- 3. Save to File ---
        plt.savefig(output_path)
        print(f"Bar graph saved successfully to '{output_path}'")

    except Exception as e:
        print(f"An error occurred while creating the bar graph: {e}")
    finally:
        plt.close()

def create_map_plot(dataset, lon_var, lat_var, value_var, title='Map Plot', output_path='map_plot.png'):
    """Generates a geographic map plot from an xarray Dataset."""
    # --- 1. Input Validation ---
    if not all(v in dataset.variables for v in [lon_var, lat_var, value_var]):
        print("Error: One or more specified variables not found in the dataset.")
        return

    # --- 2. Data Preparation ---
    try:
        # Convert the entire xarray dataset to a pandas DataFrame.
        df = dataset.to_dataframe().reset_index()

        # Create geometric points for each lat/lon pair. This is the core of GeoPandas.
        geometry = [Point(xy) for xy in zip(df[lon_var], df[lat_var])]

        # Create the GeoDataFrame. EPSG:4326 is the standard for GPS coordinates (WGS 84).
        gdf = geopandas.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

        # --- 3. Plotting Logic ---
        # Load the world map from our local, bundled shapefile for reliability.
        world_map_path = os.path.join(os.path.dirname(__file__), '..', 'map_data', 'ne_110m_admin_0_countries.shp')
        world = geopandas.read_file(world_map_path)

        # Create the plot figure and axes.
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))

        # Plot the base map layer.
        world.plot(ax=ax, color='lightgray', edgecolor='black')

        # Plot our hurricane data on top of the map.
        # The 'value_var' column is used to determine the color of each point.
        gdf.plot(value_var, ax=ax, legend=True, markersize=50, alpha=0.7,
                 cmap='autumn_r', legend_kwds={'label': value_var, 'orientation': "horizontal"})

        plt.title(title, fontsize=18, weight='bold')
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.grid(True)

        # --- 4. Save to File ---
        plt.savefig(output_path, bbox_inches='tight')
        print(f"Map plot saved successfully to '{output_path}'")

    except Exception as e:
        print(f"An error occurred while creating the map plot: {e}")
    finally:
        plt.close()
