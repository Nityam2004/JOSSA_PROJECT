import pandas as pd

# Load the CSV file
file_path = 'st.csv'
df = pd.read_csv(file_path)

# Remove commas from the 'Rank' column
df['Rank'] = df['Rank'].str.replace(',', '').astype(float)

# Save the modified DataFrame back to CSV, overwriting the original file
df.to_csv('st.csv', index=False)
