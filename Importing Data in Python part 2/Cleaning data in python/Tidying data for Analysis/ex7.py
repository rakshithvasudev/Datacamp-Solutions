"""
Print the index of airquality_pivot by accessing its .index attribute. This has been done for you.
Reset the index of airquality_pivot using its .reset_index() method.
Print the new index of airquality_pivot.
Print the head of airquality_pivot.
"""
# Print the index of airquality_pivot
print(airquality_pivot.index)

# Reset the index of airquality_pivot: airquality_pivot_reset
airquality_pivot_reset = airquality_pivot.reset_index()

# Print the new index of airquality_pivot_reset
print(airquality_pivot_reset.index)

# Print the head of airquality_pivot_reset
print(airquality_pivot_reset.head())

