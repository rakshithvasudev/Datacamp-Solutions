"""
Print the head of airquality.
Use pd.melt() to melt the Ozone, Solar.R, Wind, and Temp columns of airquality into rows. Do this by using id_vars to specify the columns you do not wish to melt: 'Month' and 'Day'.
Print the head of airquality_melt.
"""
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality,id_vars=['Month','Day'])

# Print the head of airquality_melt
print(airquality_melt.head())
