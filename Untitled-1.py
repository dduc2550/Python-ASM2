
import pandas as pd

# Read data from CSV files
data = pd.read_csv('sales_data-1.csv', )
data1 = pd.read_csv('sales_data-2.csv', )


# Handle missing values
# Check for missing values
missing_values = data.isna().sum()
# Remove rows with missing values
data.dropna(inplace=True)



# Remove duplicate data
# Remove duplicate data based on all columns
data.drop_duplicates(inplace=True)


# Data normalization
# Normalize the 'ProductName' column to capitalize the first letter
data['ProductName'] = data['ProductName'].str.capitalize()


# Handle outliers
# Handle outliers in the 'Quantity' column
data = data[data['Quantity'] <= 100]


# Combine data from two DataFrames
combined_data = pd.concat([data, data1], ignore_index=True)


# Save data to new CSV files
data.to_csv('processed_sales_data.csv', index=False)
# Save the resulting DataFrame to a CSV file
combined_data.to_csv('processed_sales_data.csv', index=False)

print('Data processing successful !!!')