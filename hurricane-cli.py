#!/usr/bin/env python
# hurricane_cli.py

import argparse
from hurricane_analyzer.data_loader import load_data
from hurricane_analyzer.visualizer import create_pie_chart, create_bar_graph, create_map_plot

def handle_plot_command(args):
    """
    Handles all logic for the 'plot' command. It loads the data
    and then calls the appropriate visualization function.
    """
    print("--- Hurricane Plotting Tool ---")

    # --- 1. Load Data ---
    print(f"Loading data from: {args.input}")
    dataset = load_data(args.input)
    if dataset is None:
        print("Failed to load data. Aborting.")
        return

    # --- 2. Dispatch to the correct plotting function ---
    # Determine a sensible default title if one isn't provided.
    title = args.title if args.title else f"Hurricane Data Visualization"

    if args.type == 'pie':
        if not args.variable:
            print("Error: --variable is required for pie charts.")
            return
        create_pie_chart(dataset, variable=args.variable, title=title, output_path=args.output)

    elif args.type == 'bar':
        if not args.variable or not args.y_variable:
            print("Error: --variable (x-axis) and --y-variable are required.")
            return
        create_bar_graph(dataset, x_variable=args.variable, y_variable=args.y_variable, title=title, output_path=args.output)

    elif args.type == 'map':
        if not args.lon_var or not args.lat_var or not args.variable:
            print("Error: --lon-var, --lat-var, and --variable (for color) are required for map plots.")
            return
        create_map_plot(dataset, lon_var=args.lon_var, lat_var=args.lat_var, value_var=args.variable, title=title, output_path=args.output)

def main():
    """
    Main entry point for the hurricane CLI tool.
    Sets up the argument parser and delegates to the appropriate handler.
    """

    # The main parser is the top-level container for our CLI.
    parser = argparse.ArgumentParser(
        description="A command-line tool for analyzing and visualizing hurricane data."
    )
    # Subparsers allow us to have distinct commands (like 'plot', 'analyze', etc.)
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    # --- 'plot' Command Parser ---
    # This parser handles all arguments related to the 'plot' command.
    plot_parser = subparsers.add_parser('plot', help='Generate a plot from a data file.')

    # --- Define Arguments for the 'plot' command ---
    plot_parser.add_argument('--type', type=str, required=True, choices=['pie', 'bar', 'map'], help='The type of plot to generate.')
    plot_parser.add_argument('--input', type=str, required=True, help='Path to the input data file (CSV, netCDF, HDF5).')
    plot_parser.add_argument('--output', type=str, required=True, help='Path to save the output plot image.')
    plot_parser.add_argument('--title', type=str, help='Optional title for the plot.')

    # Arguments for specific plot types, grouped for clarity.
    plot_parser.add_argument('--variable', type=str, help='The primary data variable to plot.')
    plot_parser.add_argument('--y-variable', type=str, help='The y-axis variable for bar charts.')
    plot_parser.add_argument('--lon-var', type=str, help='The longitude variable for map plots.')
    plot_parser.add_argument('--lat-var', type=str, help='The latitude variable for map plots.')

    # Parse the command-line arguments provided by the user.
    args = parser.parse_args()

    # --- Command Delegation ---
    # Based on the command, call the appropriate handler function.
    if args.command == 'plot':
        handle_plot_command(args)
    else:
        # If no command is given, the user likely needs help.
        parser.print_help()

# This is the standard entry point for a Python script.
if __name__ == '__main__':
    main()
