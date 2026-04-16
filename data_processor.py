import pandas as pd

# Load the three CSV files
file1 = pd.read_csv('./data/daily_sales_data_0.csv')
file2 = pd.read_csv('./data/daily_sales_data_1.csv')
file3 = pd.read_csv('./data/daily_sales_data_2.csv')

# Mix them all into one giant spreadsheet
all_data = pd.concat([file1, file2, file3])

# Filter for Pink Morsels
pink_morsels = all_data[all_data['product'] == 'pink morsel'].copy()

# Strip the '$' sign and calculate Sales = Price * Quantity
pink_morsels['price'] = pink_morsels['price'].str.replace('$', '').astype(float)
pink_morsels['sales'] = pink_morsels['price'] * pink_morsels['quantity']

# Keep only the requested columns
final_data = pink_morsels[['sales', 'date', 'region']]

# Save the final product to a new file
final_data.to_csv('formatted_daily_sales.csv', index=False)

print("Success! Your data is squished and saved as formatted_daily_sales.csv")
