"""See the power of a recommendation engine
Taylor and Jane both like watching movies. Taylor only likes dramas, comedies and romances. 
Jane likes only action, adventure and otherwise exciting films. 
One of the greatest benefits of ALS-based recommendation engines is that they can 
identify movies or items that users will like, even if they themselves think that they might not like them. Take a look at the movie ratings that Taylor and Jane have provided below. It would stand to reason that their different preferences would generate different recommendations.

Instructions
100 XP
Take a look at TJ_ratings using the .show() method and any other methods you prefer, to see how each of them rated the various movies they've seen.
Input user names into the get_ALS_recs function provided to see what movies ALS recommends for Jane and Taylor based on the ratings provided. Do the ratings make sense to you?
"""

# View TJ_ratings
TJ_ratings.show()

# Generate recommendations for users
get_ALS_recs(["Taylor","Jane"]) 