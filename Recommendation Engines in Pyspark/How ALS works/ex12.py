"""
Assigning integer id's to movies
Let's now do the same thing to the movies. Then let's join the new user id's and movie id's into one dataframe.

Instructions
100 XP
Use the .select() and the .distinct() methods to extract all unique Movie's from the ratings dataframe.
Repartition the movies dataframe to one partition using the coalesce() method.
Complete the partial code provided to assign unique integer id's to each movie. Name the new column movieId and call the .persist() method on the resulting dataframe.
Join the ratings dataframe to the users dataframe and subsequently to the movies dataframe. Call the result movie_ratings.

"""

# Extract the distinct movie id's
movies = ratings.select("Movie").distinct() 

# Repartition the data to have only one partition.
movies = movies.coalesce(1) 

# Create a new column of movieId integers. 
movies = movies.withColumn("movieId", monotonically_increasing_id()).persist() 

# Join the ratings, users and movies dataframes
movie_ratings = ratings.join(users, "User", "left").join(movies, "Movie", "left")
movie_ratings.show()