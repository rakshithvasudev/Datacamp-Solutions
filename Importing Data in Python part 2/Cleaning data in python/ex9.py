"""
Using the .boxplot() method of df, create a boxplot of 'initial_cost' across the different values of 'Borough'.
Display the plot.
"""
# Import necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# Create the boxplot
df.boxplot(column='initial_cost', by='Borough', rot=90)

# Display the plot
plt.show()
