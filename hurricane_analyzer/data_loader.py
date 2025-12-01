# hurricane_analyzer/data_loader.py

import os
import pandas as pd
import xarray as xr

def load_data(filepath):
    """
    Loads data from various formats (CSV, netCDF, HDF5) into a unified
    xarray Dataset. This function automatically detects the file type
    based on its extension.

    For netCDF/HDF5 files, it also automatically applies scaling
    factors and offsets if they are present as variable attributes.

    Args:
        filepath (str): The path to the data file.

    Returns:
        xarray.Dataset: The loaded data, converted to an xarray Dataset,
                        or None if the file format is not supported or an
                        error occurs.
    """
    # --- Input Validation ---
    if not isinstance(filepath, str) or not os.path.exists(filepath):
        print(f"Error: Filepath '{filepath}' not found or is not a valid path.")
        return None

    # --- File Type Detection ---
    _, extension = os.path.splitext(filepath)
    extension = extension.lower()

    try:
        if extension == '.csv':
            # Convert pandas DataFrame to xarray Dataset
            df = pd.read_csv(filepath)
            dataset = xr.Dataset.from_dataframe(df)
            print(f"Successfully loaded CSV file: {filepath}")
            return dataset

        elif extension in ['.nc', '.nc4']:
            # Load netCDF file directly with xarray
            # `decode_cf` is True by default, handling scaling/offsets
            dataset = xr.open_dataset(filepath, decode_cf=True)
            print(f"Successfully loaded netCDF file: {filepath}")
            return dataset

        elif extension in ['.h5', '.hdf5']:
            # Load HDF5 file using the netcdf4 engine
            # This also benefits from xarray's automatic decoding
            dataset = xr.open_dataset(filepath, engine='h5netcdf', decode_cf=True)
            print(f"Successfully loaded HDF5 file: {filepath}")
            return dataset

        else:
            print(f"Error: Unsupported file format '{extension}'.")
            print("Supported formats are: .csv, .nc, .nc4, .h5, .hdf5")
            return None

    except Exception as e:
        print(f"An unexpected error occurred while loading '{filepath}': {e}")
        return None
