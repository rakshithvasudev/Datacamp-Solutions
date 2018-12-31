"""
The GroupBy and Filter Methods
Now that we know a little more about the dataset, let's look at some general summary metrics of the ratings dataset and see how many ratings the movies have and how many ratings the users have provided. Two common methods that will be helpful to you as you perform summary statistics in Spark are the .filter() and the .groupBy() methods. The .filter() method allows you to filter out any data that doesn't meet your specified criteria.

Instructions
100 XP
Import col from the pyspark.sql.functions, and view the ratings dataset using the .show().
Apply the .filter() method on the ratings dataset with the following filter inside the parenthesis in order to include only userId's less than 100: col("userId") < 100.
Call the .groupBy() method on the ratings dataset to group the data by userId. Call the .count() method to see how many movies each userId has rated.
Take Hint (-30 XP)
"""

# Import the requisite packages
from pyspark.sql.functions import col

# View the ratings dataset
ratings.show()

# Filter out all userIds greater than 100
ratings.filter(col("userId") < 100).show()

# Group data by userId, count ratings
ratings.groupBy("userId").count().show()
