import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def load_data(file_path):
    """
    Loads the CSV file into a pandas DataFrame.
    """
    return pd.read_csv(file_path)

def clean_data(df):
    """
    Cleans the data by handling missing values and ensuring appropriate data types.
    """
    df.columns = ['Name', 'Date', 'Weight', 'Type', 'Characteristic', 'Additional_Info']
    df = df.drop(columns=['Additional_Info'])
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna()
    df['Weight'] = df['Weight'].astype(float)
    return df

def calculate_average_price(df, species):
    """
    Calculates the average price of pets in the specified species.
    """
    species_df = df[df['Type'].str.lower() == species.lower()]
    if species_df.empty:
        return 0.0
    average_price = species_df['Weight'].mean()
    return average_price

def find_pets_with_feature(df, feature):
    """
    Finds the names of pets with the specified special feature.
    """
    feature_df = df[df['Characteristic'].str.contains(feature, case=False, na=False)]
    return feature_df['Name'].tolist()

def get_species_statistics(df):
    """
    Returns a dictionary with species names as keys and their respective average prices and average ages as values.
    """
    species_stats = {}
    current_year = pd.Timestamp.now().year

    for species in df['Type'].unique():
        species_df = df[df['Type'] == species]
        average_price = species_df['Weight'].mean()
        average_age = species_df['Date'].apply(lambda x: current_year - x.year).mean()
        species_stats[species] = {'Average Price': average_price, 'Average Age': average_age}

    return species_stats

def plot_price_distribution(df):
    """
    Plots the distribution of prices using a histogram and saves the plot as price_distribution.png.
    """
    plt.figure(figsize=(10, 6))
    plt.hist(df['Weight'], bins=20, color='blue', edgecolor='black')
    plt.title('Price Distribution of Pets')
    plt.xlabel('Price')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.savefig('price_distribution.png')
    plt.close()

def plot_average_price_by_species(df):
    """
    Plots the average price by species using a bar chart and saves the plot as average_price_by_species.png.
    """
    average_prices = df.groupby('Type')['Weight'].mean().sort_values()
    
    plt.figure(figsize=(12, 8))
    average_prices.plot(kind='bar', color='green', edgecolor='black')
    plt.title('Average Price by Species')
    plt.xlabel('Species')
    plt.ylabel('Average Price')
    plt.xticks(rotation=45)
    plt.grid(axis='y')
    plt.savefig('average_price_by_species.png')
    plt.close()

def plot_price_vs_age(df):
    """
    Plots a scatter plot of price vs. age using Seaborn.
    Saves the plot as price_vs_age.png.
    """
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=(pd.Timestamp.now().year - df['Date'].dt.year), y='Weight', data=df, hue='Type', palette='Set2', edgecolor='w', s=100)
    plt.title('Price vs. Age of Pets')
    plt.xlabel('Age (years)')
    plt.ylabel('Price')
    plt.savefig('price_vs_age.png')
    plt.close()

def plot_age_distribution_by_species(df):
    """
    Plots the distribution of ages for each species using a box plot with Plotly.
    Saves the plot as age_distribution_by_species.png.
    """
    fig = px.box(df, x='Type', y=df['Date'].dt.year, points="all")
    fig.update_layout(
        title='Age Distribution by Species',
        xaxis_title='Species',
        yaxis_title='Age (Year)',
        xaxis={'categoryorder':'mean ascending'}
    )
    fig.write_image('age_distribution_by_species.png')
