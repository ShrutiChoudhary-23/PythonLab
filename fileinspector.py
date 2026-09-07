import pandas as pd

# Take file name from user
file = input("Enter CSV/TSV file name: ")

# Read the file
df = pd.read_csv(file)

# Display basic information
print("\nDataset:")
print(df)

print("\nRows and Columns:", df.shape)
print("\nData Types:")
print(df.dtypes)

# Filter rows using a condition
column = input("\nEnter column name for filtering: ")
value = float(input("Enter minimum value: "))

filtered = df[df[column] >= value]

# Display filtered data
print("\nFiltered Data:")
print(filtered)

# Export filtered data
filtered.to_csv("cleaned_data.csv", index=False)

print("\nFiltered data saved as cleaned_data.csv")