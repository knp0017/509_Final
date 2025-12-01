import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import folium


def load_data(filepath):
    """Load data from a specified CSV file.

    This function reads a CSV file into a pandas DataFrame, providing
    robust error handling for common file-related issues.

    Parameters
    ----------
    filepath : str
        The full path to the CSV file to be loaded.

    Returns
    -------
    pandas.DataFrame or None
        A pandas DataFrame containing the loaded data if successful.
        Returns None if the file is not found, cannot be read, or is
        not a valid CSV file.

    Examples
    --------
    >>> import pandas as pd
    >>> from hurricane_analyzer.visualizer import load_data
    >>>
    >>> # Create a dummy CSV file for the example
    >>> dummy_data = {'city': ['Miami', 'Houston'], 'damage': [100, 200]}
    >>> dummy_df = pd.DataFrame(dummy_data)
    >>> dummy_df.to_csv("dummy_hurricane_data.csv", index=False)
    >>>
    >>> # Load the data using the function
    >>> df = load_data("dummy_hurricane_data.csv")
    >>> print(df)
        city  damage
    0   Miami     100
    1  Houston     200
    >>>
    >>> # Example of a failed load (non-existent file)
    >>> df_fail = load_data("non_existent_file.csv")
    >>> print(df_fail)
    None
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

def create_pie_chart(data, column, title="Pie Chart", output_path=None,
                       figsize=(10, 10), autopct="%1.1f%%", startangle=90,
                       **kwargs):
    """Generate a pie chart from a specified DataFrame column.

    This function creates a pie chart to visualize the distribution of
    categorical data. It offers extensive customization and returns the
    matplotlib figure and axes objects for further modification.

    Parameters
    ----------
    data : pandas.DataFrame
        The DataFrame containing the data to be plotted.
    column : str
        The name of the column in the DataFrame to be visualized.
        This column should contain categorical data.
    title : str, optional
        The title to be displayed on the pie chart.
        Defaults to "Pie Chart".
    output_path : str or None, optional
        The file path where the generated pie chart image will be saved.
        If None, the chart is not saved to a file. Defaults to None.
    figsize : tuple, optional
        A tuple specifying the width and height of the figure in inches.
        Defaults to (10, 10).
    autopct : str, optional
        A string or function used to label the wedges with their numeric
        value. The label will be placed inside the wedge.
        Defaults to "%1.1f%%".
    startangle : float, optional
        The angle by which the start of the first wedge is rotated
        counterclockwise from the x-axis. Defaults to 90.
    **kwargs
        Additional keyword arguments to be passed directly to the
        `matplotlib.pyplot.pie` function for further customization (e.g.,
        `colors`, `explode`).

    Returns
    -------
    tuple of (matplotlib.figure.Figure, matplotlib.axes.Axes) or (None, None)
        A tuple containing the matplotlib Figure and Axes objects for the
        generated plot. Returns (None, None) if input validation fails.

    Examples
    --------
    >>> import pandas as pd
    >>> from hurricane_analyzer.visualizer import create_pie_chart
    >>>
    >>> # 1. Basic Example: Create and save a pie chart
    >>> data = {'state': ['FL', 'FL', 'TX', 'LA', 'FL', 'TX']}
    >>> df = pd.DataFrame(data)
    >>> fig, ax = create_pie_chart(df, 'state',
    ...                            title="Hurricane Landfalls by State",
    ...                            output_path="landfalls.png")
    >>> # The chart is saved to "landfalls.png"
    >>>
    >>> # 2. Advanced Example: Customize and further modify the plot
    >>> explode_effect = (0.1, 0, 0) # Emphasize the first slice
    >>> fig, ax = create_pie_chart(df, 'state',
    ...                            title="Landfalls (Highlighted)",
    ...                            explode=explode_effect,
    ...                            shadow=True)
    >>> # Use the returned objects to add a custom annotation
    >>> if fig and ax:
    ...     ax.text(0, -1.2, "Data Source: Fictional Hurricane Center",
    ...             ha='center', fontsize=8)
    ...     # To display in an interactive session, you would use:
    ...     # fig.show()
    """
    # --- Input Validation ---
    if not isinstance(data, pd.DataFrame):
        print("Error: 'data' must be a pandas DataFrame.")
        return None, None
    if not isinstance(column, str) or column not in data.columns:
        print(f"Error: Column '{column}' not found in the DataFrame.")
        return None, None

    # --- Plotting Logic ---
    try:
        value_counts = data[column].value_counts()
        fig, ax = plt.subplots(figsize=figsize)

        ax.pie(value_counts, labels=value_counts.index, autopct=autopct,
               startangle=startangle, **kwargs)

        ax.set_title(title, fontsize=16, weight='bold')
        ax.axis('equal')  # Ensures the pie chart is circular.

        # --- Save to File ---
        if output_path:
            if isinstance(output_path, str):
                try:
                    fig.savefig(output_path, bbox_inches='tight')
                except Exception as e:
                    print(f"Error saving figure to '{output_path}': {e}")
            else:
                print("Warning: 'output_path' was not a valid string. Figure not saved.")

        return fig, ax
    except Exception as e:
        print(f"An unexpected error occurred during plot generation: {e}")
        return None, None
    finally:
        # Close the plot to free up memory, important for library functions
        if 'fig' in locals():
            plt.close(fig)

def create_bar_graph(data, x_column, y_column):
    """Generates a bar graph."""
    pass

def create_map_plot(data, lat_column, lon_column, popup_column):
    """Generates a map plot."""
    pass
