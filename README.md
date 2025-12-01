# Hurricane Data Analyzer CLI

## Overview

The Hurricane Data Analyzer is a powerful, command-line interface (CLI) tool for visualizing complex hurricane data. It is designed to work with both simple CSV files and advanced scientific data formats like NetCDF, making it a versatile tool for researchers, meteorologists, and data scientists.

This tool can generate a variety of high-quality plots, including pie charts, bar graphs, and sophisticated geographic maps.

## Installation

To use the Hurricane Data Analyzer, you first need to install its dependencies.

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

The primary entry point for the tool is the `hurricane-cli.py` script. The main command is `plot`, which takes several arguments to specify the desired visualization.

### General Syntax

```bash
python hurricane-cli.py plot --type <plot_type> --input <file> --output <file> [options...]
```

### Example 1: Creating a Pie Chart from a NetCDF File

This example demonstrates how to create a pie chart of storm names from our sample NetCDF file.

```bash
python hurricane-cli.py plot \
    --type pie \
    --input sample_data.nc \
    --output storm_distribution.png \
    --variable storm_name \
    --title "Distribution of Major Hurricanes"
```

### Example 2: Creating a Bar Graph from a NetCDF File

This example shows how to plot the raw (unscaled) maximum wind speed for each storm.

```bash
python hurricane-cli.py plot \
    --type bar \
    --input sample_data.nc \
    --output wind_speeds.png \
    --variable storm_name \
    --y-variable max_wind_speed_raw \
    --title "Max Wind Speed by Storm"
```

### Example 3: Creating an Advanced Map Plot

This example demonstrates the tool's most powerful feature: plotting the scaled wind speed data on a geographic map. Our data loader will automatically apply the `scale_factor` and `add_offset` from the NetCDF file.

First, you need to tell the tool to use the corrected variable, which `xarray` creates automatically. We will name it `max_wind_speed_raw` as that is the raw data name. **Note:** The plotting function will use the *scaled* data for the colors, not the raw integers.

```bash
python hurricane-cli.py plot \
    --type map \
    --input sample_data.nc \
    --output hurricane_tracks_map.png \
    --lon-var longitude \
    --lat-var latitude \
    --variable max_wind_speed_raw \
    --title "Hurricane Positions and Scaled Wind Speeds"
```
