import os
import sys
import pandas as pd

# Add the project's root directory to the Python path to allow importing 'hurricane_analyzer'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from hurricane_analyzer import visualizer

def run_pie_chart_demo():
    """
    Demonstrates the usage of the create_pie_chart function.
    """
    print("--- Running Pie Chart Example ---")

    # 1. Create a sample DataFrame
    sample_hurricane_data = {
        'state': ['Florida', 'Texas', 'Louisiana', 'Florida', 'Texas', 'Florida'],
        'damage_usd': [1000, 3500, 1200, 2000, 4000, 500]
    }
    df_sample = pd.DataFrame(sample_hurricane_data)

    print("\nSample Data:")
    print(df_sample)

    # 2. Define the output path for the chart
    # To keep the root directory clean, save the output in the 'examples' folder
    output_path = os.path.join(os.path.dirname(__file__), 'example_pie_chart.png')


    # 3. Use the create_pie_chart function to generate the plot
    print(f"\nGenerating example pie chart at '{output_path}'...")
    visualizer.create_pie_chart(
        df_sample,
        'state',
        title='Example: Hurricane Landfalls by State',
        output_path=output_path
    )

    # 4. Verify that the file was created
    if os.path.exists(output_path):
        print(f"\nSuccessfully created chart: {output_path}")
    else:
        print(f"\nError: Chart was not created at {output_path}")


    print("\n--- Example finished ---")

if __name__ == "__main__":
    run_pie_chart_demo()
