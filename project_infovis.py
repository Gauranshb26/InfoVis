import pandas as pd

# Load the CSV file
file_path = "US census bureau table.csv"
df = pd.read_csv(file_path)

# Identify relevant row indices
value_row_index = 9  # Corrected row index for median house value
income_row_index = df[df.iloc[:, 0].str.contains("Median household income", na=False, case=False)].index[0]

# Extract state names from column headers
state_names = [col.split("!!")[0] for col in df.columns[1::4]]  # Extract unique state names

# Extract values for median house value and median household income
median_house_values = df.iloc[value_row_index, 1::4].astype(str).str.replace(",", "", regex=True).apply(pd.to_numeric, errors='coerce')
median_household_incomes = df.iloc[income_row_index, 1::4].astype(str).str.replace(",", "", regex=True).apply(pd.to_numeric, errors='coerce')

# Compute the average ratio of VALUE to Household Income 
value_to_income_ratio = median_house_values / median_household_incomes
value_to_income_ratio.replace([float('inf'), -float('inf')], None, inplace=True)  

# Create a cleaned DataFrame
cleaned_df = pd.DataFrame({
    "State": state_names,
    "Median House Value": median_house_values.values,
    "Median Household Income": median_household_incomes.values,
    "Value to Income Ratio": value_to_income_ratio.values
})

# Save to a new CSV file
cleaned_file_path = "cleaned_housing_data.csv"
cleaned_df.to_csv(cleaned_file_path, index=False)

# Display the cleaned data
print(cleaned_df.head())
