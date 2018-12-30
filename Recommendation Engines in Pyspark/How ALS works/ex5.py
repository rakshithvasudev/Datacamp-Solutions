"""
Matrix Factorization
Matrix G is provided here as a Pandas dataframe. View it to understand what it looks like. Look at the possible factor matrices H, I, and J (also Pandas dataframes), and determine which two matrices will produce the matrix G when mutliplied together.

Instructions
100 XP
Take a look at matrix G using the print command
Take a look at the matrices H, I, and J and determine which pair of those matrices will produce G when multiplied together.
Input your answer into the np.matmul() code provided.
Take Hint (-30 XP)
"""
# Take a look at Matrix G using the following print function
print("Matrix G:")
print(G)

# Take a look at the matrices H, I, and J and determine which pair of those matrices will produce G when multiplied together. 
print("Matrix H:")
print(H)
print("Matrix I:")
print(I)
print("Matrix J:")
print(J)

# Multiply the two matrices that are factors of the matrix G
prod = np.matmul(H, J)
print(G == prod)