"""
Print the head of airquality_melt.
Pivot airquality_melt by using .pivot_table() with the rows indexed by 'Month' and 'Day', the columns indexed by 'measurement', and the values populated with 'reading'.
Print the head of airquality_pivot.
"""

# Print the head of airquality_melt
print(airquality_melt.head())

# Pivot airquality_melt: airquality_pivot
airquality_pivot = pd.pivot_table(data=airquality_melt,index=['Month','Day'], columns='measurement', values='reading')

# Print the head of airquality_pivot
print(airquality_pivot.head())
