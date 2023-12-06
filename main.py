import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import pandas as pd

def load_and_organize_dataset(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)
    # Drop rows where 'ESTIMATE' column has NaN values
    data = data.dropna(subset=['ESTIMATE'])

    # Selecting relevant columns: 'STUB_NAME', 'STUB_LABEL', 'AGE', 'YEAR', and 'ESTIMATE'
    selected_columns = ['STUB_NAME', 'STUB_LABEL', 'AGE', 'YEAR', 'ESTIMATE']
    organized_data = data[selected_columns]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.width', None)
    # Sort the data
    organized_data = organized_data.sort_values(by=['YEAR', 'STUB_NAME', 'AGE'])

    # Display a subset of the organized DataFrame for inspection
    print("\nOrganized Dataset Subset by Year, STUB_NAME, and Age:")
    print(organized_data.head(20))
def men_old(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Filter data based on the condition
    df = data[(data['STUB_LABEL_NUM'] == 5.114) | (data['STUB_LABEL_NUM'] == 5.124) | (data['STUB_LABEL_NUM'] == 5.134) | (data['STUB_LABEL_NUM'] == 5.144)]

    # Selecting relevant columns: 'STUB_NAME', 'STUB_LABEL', 'AGE', 'YEAR', and 'ESTIMATE'
    selected_columns = ['STUB_NAME', 'STUB_LABEL', 'AGE', 'YEAR', 'ESTIMATE']
    organized_data = df[selected_columns]

    # Sort the data
    organized_data = organized_data.sort_values(by=['YEAR', 'STUB_NAME', 'AGE'])

    # Get distinct 'STUB_LABEL' values
    stub_labels = organized_data['STUB_LABEL'].unique()

    # Set up a color cycle for distinct colors
    color_cycle = cycle(plt.cm.tab10.colors)

    # Plotting
    fig, ax = plt.subplots(figsize=(18, 8))  # Adjust the figure size as needed

    # Assuming you want to create a grouped bar chart for each unique 'STUB_LABEL'
    bar_width = 0.2  # Adjust the width of the bars
    separation = 0.4  # Adjust the separation between groups
    num_labels = len(stub_labels)

    for i, stub_label in enumerate(stub_labels):
        group = organized_data[organized_data['STUB_LABEL'] == stub_label]
        x_positions = np.arange(len(group['YEAR'])) + i * (bar_width + separation)
        ax.bar(x_positions, group['ESTIMATE'], width=bar_width, label=stub_label, color=next(color_cycle))

    # labels and title
    plt.title("Grouped Bar Graph")
    plt.xlabel("Year")
    plt.ylabel("Estimate")

    # Adjust x-axis ticks and labels
    ax.set_xticks(np.arange(len(organized_data['YEAR'].unique())) + (len(stub_labels) - 1) * (bar_width + separation) / 2)
    ax.set_xticklabels(organized_data['YEAR'].unique(), rotation=45, ha="right")

    # legend
    plt.legend()

    plt.show()

def men_young(file_path):
    # Load the dataset
    data = pd.read_csv(file_path)

    # Filter data based on the condition
    df = data[(data['STUB_LABEL_NUM'] == 5.113) | (data['STUB_LABEL_NUM'] == 5.123) | (data['STUB_LABEL_NUM'] == 5.133) | (data['STUB_LABEL_NUM'] == 5.143)]

    # Selecting relevant columns: 'STUB_NAME', 'STUB_LABEL', 'AGE', 'YEAR', and 'ESTIMATE'
    selected_columns = ['STUB_NAME', 'STUB_LABEL', 'AGE', 'YEAR', 'ESTIMATE']
    organized_data = df[selected_columns]

    # Sort the data
    organized_data = organized_data.sort_values(by=['YEAR', 'STUB_NAME', 'AGE'])

    # Get distinct 'STUB_LABEL' values
    stub_labels = organized_data['STUB_LABEL'].unique()

    # Set up a color cycle for distinct colors
    color_cycle = cycle(plt.cm.tab10.colors)

    # Plotting
    fig, ax = plt.subplots(figsize=(18, 8))  # Adjust the figure size as needed

    # Assuming you want to create a grouped bar chart for each unique 'STUB_LABEL'
    bar_width = 0.2  # Adjust the width of the bars
    separation = 0.4  # Adjust the separation between groups
    num_labels = len(stub_labels)

    for i, stub_label in enumerate(stub_labels):
        group = organized_data[organized_data['STUB_LABEL'] == stub_label]
        x_positions = np.arange(len(group['YEAR'])) + i * (bar_width + separation)
        ax.bar(x_positions, group['ESTIMATE'], width=bar_width, label=stub_label, color=next(color_cycle))

    # labels and title
    plt.title("Grouped Bar Graph")
    plt.xlabel("Year")
    plt.ylabel("Estimate")

    # Adjust x-axis ticks and labels
    ax.set_xticks(np.arange(len(organized_data['YEAR'].unique())) + (len(stub_labels) - 1) * (bar_width + separation) / 2)
    ax.set_xticklabels(organized_data['YEAR'].unique(), rotation=45, ha="right")

    # legend
    plt.legend()

    plt.show()
def main():
    file_path = 'Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv'
    load_and_organize_dataset(file_path)
    men_old(file_path)
    men_young(file_path)

if __name__ == "__main__":
    main()


