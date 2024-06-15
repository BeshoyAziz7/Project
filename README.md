-----------------------Running the Project--------------------------
Make sure you have Python installed .
Install required packages using pip if they are not already installed
Have main.py and pet_analysis.py in the same directory.
Place CSV data file (pets.csv) in the same directory as main.py.
--------------------Explanation of Each Script------------------------
1--------------------------main.py------------------------------------------------
Uses pa.load_data(file_path) to load the CSV file into a DataFrame (df).
Cleans the data using pa.clean_data(df) to handle missing values and convert data types appropriately.
pa.calculate_average_price(cleaned_df, species) to compute the average price of pets belonging to a specific species.
pa.find_pets_with_feature(cleaned_df, feature) to find pets with a specific feature.
pa.get_species_statistics(cleaned_df) to retrieve statistics such as average price and average age for each species.
pa.plot_price_distribution(cleaned_df): Generates a histogram of price distribution and saves it as price_distribution.png.
pa.plot_average_price_by_species(cleaned_df): Creates a bar chart showing average price by species and saves it as average_price_by_species.png.
pa.plot_price_vs_age(cleaned_df): Plots a scatter plot of price vs. age using Seaborn and saves it as price_vs_age.png.
pa.plot_age_distribution_by_species(cleaned_df): Would plot age distribution by species using Plotly and save it as age_distribution_by_species.png.
2--------------------------pet_analysis.py------------------------------------
load_data(file_path): Loads a CSV file into a pandas DataFrame.
clean_data(df): Cleans the DataFrame by renaming columns, handling missing values, and converting data types.
calculate_average_price(df, species): Calculates the average price of pets for a specified species.
find_pets_with_feature(df, feature): Finds pets with a specific feature.
get_species_statistics(df): Computes average price and average age statistics for each species.
plot_price_distribution(df): Creates a histogram of price distribution.
plot_average_price_by_species(df): Generates a bar chart of average price by species.
plot_price_vs_age(df): Plots a scatter plot of price vs. age using Seaborn.
plot_age_distribution_by_species(df): Would plot age distribution by species using Plotly.







