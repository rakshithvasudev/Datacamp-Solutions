"""
Using df, create a scatter plot (kind='scatter') with 'initial_cost' on the x-axis and the 'total_est_fee' on the y-axis. Rotate the x-axis labels by 70 degrees.
Create another scatter plot exactly as above, substituting df_subset in place of df.

"""

# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create and display the first scatter plot
df.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()

# Create and display the second scatter plot
df_subset.plot(kind='scatter', x='initial_cost', y='total_est_fee', rot=70)
plt.show()