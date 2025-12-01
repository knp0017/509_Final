# hurricane_analyzer/visualizer.py

import os
import matplotlib.pyplot as plt
import seaborn as sns
import xarray as xr
import geopandas
from shapely.geometry import Point

def create_pie_chart(dataset, variable, title='Pie Chart', output_path='pie_chart.png'):
    """
    Generates a pie chart from a specified variable in an xarray Dataset.

    Args:
        dataset (xarray.Dataset): The dataset containing the data.
        variable (str): The name of the variable to plot.
        title (str, optional): The title for the chart.
        output_path (str, optional): The path to save the chart image.
    """
    if not isinstance(dataset, xr.Dataset):
        print("Error: 'dataset' must be an xarray Dataset.")
        return
    if variable not in dataset.variables:
        print(f"Error: Variable '{variable}' not found in the Dataset.")
        return
    try:
        df = dataset[variable].to_dataframe()
        value_counts = df[variable].value_counts()
        plt.figure(figsize=(10, 10))
        plt.pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
        plt.title(title, fontsize=16, weight='bold')
        plt.ylabel('')
        plt.axis('equal')
        plt.savefig(output_path, bbox_inches='tight')
        print(f"Pie chart saved successfully to '{output_path}'")
    except Exception as e:
        print(f"An error occurred while creating the pie chart: {e}")
    finally:
        plt.close()

def create_bar_graph(dataset, x_variable, y_variable, title='Bar Graph', output_path='bar_graph.png'):
    """
    Generates a bar graph from specified variables in an xarray Dataset.

    Args:
        dataset (xarray.Dataset): The dataset containing the data.
        x_variable (str): The variable for the x-axis.
        y_variable (str): The variable for the y-axis.
        title (str, optional): The title for the chart.
        output_path (str, optional): The path to save the chart image.
    """
    if not isinstance(dataset, xr.Dataset):
        print("Error: 'dataset' must be an xarray Dataset.")
        return
    if x_variable not in dataset.variables or y_variable not in dataset.variables:
        print(f"Error: One or both variables not found.")
        return
    try:
        df = dataset.to_dataframe().reset_index()
        plt.figure(figsize=(12, 7))
        sns.barplot(x=x_variable, y=y_variable, data=df, palette='viridis')
        plt.title(title, fontsize=16, weight='bold')
        plt.xlabel(x_variable, fontsize=12)
        plt.ylabel(y_variable, fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(output_path)
        print(f"Bar graph saved successfully to '{output_path}'")
    except Exception as e:
        print(f"An error occurred while creating the bar graph: {e}")
    finally:
        plt.close()

def create_map_plot(dataset, lon_var, lat_var, value_var, title='Map Plot', output_path='map_plot.png'):
    """
    Generates a geographic map plot from an xarray Dataset.

    Args:
        dataset (xarray.Dataset): Dataset with longitude, latitude, and value data.
        lon_var (str): The name of the longitude variable.
        lat_var (str): The name of the latitude variable.
        value_var (str): The name of the variable to plot as colored points.
        title (str, optional): The title for the map.
        output_path (str, optional): The path to save the map image.
    """
    if not all(v in dataset.variables for v in [lon_var, lat_var, value_var]):
        print("Error: One or more specified variables not found in the dataset.")
        return

    try:
        # Convert xarray dataset to pandas DataFrame
        df = dataset.to_dataframe().reset_index()

        # Create GeoDataFrame
        geometry = [Point(xy) for xy in zip(df[lon_var], df[lat_var])]
        gdf = geopandas.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")

        # Load the world map from the local shapefile
        world_map_path = os.path.join(os.path.dirname(__file__), '..', 'map_data', 'ne_110m_admin_0_countries.shp')
        world = geopandas.read_file(world_map_path)

        # Create the plot
        fig, ax = plt.subplots(1, 1, figsize=(15, 10))
        world.plot(ax=ax, color='lightgray', edgecolor='black')

        # Plot the data points
        gdf.plot(value_var, ax=ax, legend=True, markersize=50, alpha=0.7,
                 cmap='autumn_r', legend_kwds={'label': value_var, 'orientation': "horizontal"})

        plt.title(title, fontsize=18, weight='bold')
        ax.set_xlabel("Longitude")
        ax.set_ylabel("Latitude")
        ax.grid(True)

        plt.savefig(output_path, bbox_inches='tight')
        print(f"Map plot saved successfully to '{output_path}'")

    except Exception as e:
        print(f"An error occurred while creating the map plot: {e}")
    finally:
        plt.close()
