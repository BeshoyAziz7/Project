import pet_analysis as pa

# Load and clean the data
file_path = 'D:\Projects VS\Exam\pets.csv'
df = pa.load_data(file_path)
cleaned_df = pa.clean_data(df)

# Calculate average price for a specific species
species = 'Dog'
avg_price = pa.calculate_average_price(cleaned_df, species)
print(f"Average price of {species}s: {avg_price}")

# Find pets with a specific feature
feature = 'flies'
pets_with_feature = pa.find_pets_with_feature(cleaned_df, feature)
print(f"Pets with the feature '{feature}': {pets_with_feature}")

# Get species statistics
species_stats = pa.get_species_statistics(cleaned_df)
print("Species statistics:")
for species, stats in species_stats.items():
    print(f"{species}: {stats}")

# Plot price distribution
pa.plot_price_distribution(cleaned_df)
print("Price distribution plot saved as 'price_distribution.png'")

# Plot average price by species
pa.plot_average_price_by_species(cleaned_df)
print("Average price by species plot saved as 'average_price_by_species.png'")

# Plot price vs. age
pa.plot_price_vs_age(cleaned_df)
print("Price vs. Age plot saved as 'price_vs_age.png'")

# Plot age distribution by species
# pa.plot_age_distribution_by_species(cleaned_df)
# print("Age distribution by species plot saved as 'age_distribution_by_species.png'")

