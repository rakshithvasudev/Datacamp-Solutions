"""
Print the head of airquality.
Melt the Ozone, Solar.R, Wind, and Temp columns of airquality into rows, with the default variable column renamed to 'measurement' and the default value column renamed to 'reading'. You can do this by specifying, respectively, the var_name and value_name parameters.
Print the head of airquality_melt.
"""
#Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month','Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())
