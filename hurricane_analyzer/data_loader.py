# hurricane_analyzer/data_loader.py
"""
Handles all data loading operations for the hurricane analyzer.

This module provides a unified `load_data` function that can intelligently
handle multiple file formats, including CSV, NetCDF, and HDF5. It uses
xarray as the standard data structure to ensure compatibility with
advanced scientific data.
"""
import os
import pandas as pd
import xarray as xr

def _load_csv(filepath):
    """Loads a CSV and converts it to an xarray Dataset."""
    df = pd.read_csv(filepath)
    return xr.Dataset.from_dataframe(df)

def _load_netcdf(filepath):
    """
    Loads a NetCDF file using xarray.
    `decode_cf=True` (the default) is crucial as it automatically handles
    scaling, offsets, and time variables, converting them into useful units.
    """
    return xr.open_dataset(filepath, decode_cf=True)

def _load_hdf5(filepath):
    """
    Loads an HDF5 file using xarray with the h5netcdf engine.
    This also benefits from xarray's automatic decoding capabilities.
    """
    return xr.open_dataset(filepath, engine='h5netcdf', decode_cf=True)

def load_data(filepath):
    """
    Loads data from various formats (CSV, NetCDF, HDF5) into a unified
    xarray Dataset by dispatching to the appropriate loader.

    Args:
        filepath (str): The path to the data file.

    Returns:
        xarray.Dataset: The loaded data, or None if an error occurs.
    """
    # --- 1. Input Validation ---
    if not isinstance(filepath, str) or not os.path.exists(filepath):
        print(f"Error: Filepath '{filepath}' not found or is not a valid path.")
        return None

    # --- 2. Dispatcher Pattern for File Loading ---
    # This dictionary maps file extensions to the correct loading function.
    # It's a clean and scalable alternative to a long if/elif/else chain.
    file_loaders = {
        '.csv': _load_csv,
        '.nc': _load_netcdf,
        '.nc4': _load_netcdf,
        '.h5': _load_hdf5,
        '.hdf5': _load_hdf5,
    }

    _, extension = os.path.splitext(filepath)
    loader_func = file_loaders.get(extension.lower())

    if not loader_func:
        print(f"Error: Unsupported file format '{extension}'.")
        print(f"Supported formats are: {list(file_loaders.keys())}")
        return None

    # --- 3. Execute Loading and Handle Errors ---
    try:
        dataset = loader_func(filepath)
        print(f"Successfully loaded {extension.upper()} file: {filepath}")
        return dataset
    except Exception as e:
        print(f"An unexpected error occurred while loading '{filepath}': {e}")
        return None
