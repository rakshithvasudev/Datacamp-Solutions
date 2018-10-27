"""Import pandas as pd.
Read 'dob_job_application_filings_subset.csv' into a DataFrame called df.
Print the head and tail of df.
Print the shape of df and its columns. Note: .shape and .columns are attributes, not methods, so you don't need to follow these with parentheses ().
Hit 'Submit Answer' to view the results! Notice the suspicious number of 0 values. Perhaps these represent missing data.
"""
# Import pandas
import pandas as pd

# Read the file into a DataFrame: df
df = pd.read_csv('dob_job_application_filings_subset.csv')

# Print the head of df
print(df.head())

# Print the tail of df
print(df.tail())

# Print the shape of df
print(df.shape)

# Print the columns of df
print(df.columns)

# Print the head and tail of df_subset
print(df_subset.head())
print(df_subset.tail())
