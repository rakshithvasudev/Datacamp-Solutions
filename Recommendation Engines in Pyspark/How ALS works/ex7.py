"""
Estimating Recommendations
Use your knowledge of matrix multiplication to determine which movie will have the highest recommendation for User_3. The ratings matrix has been factorized into U and P with ALS.

Instructions 1/3
35 XP
1
2
3
View the left factor matrix, U, using the print function.

Take Hint (-10 XP)
"""

# View left factor matrix
print (U)


"""
Did you see anything interesting about User_3? Now inspect the right factor matrix, P. Use the print function.
"""


# View right factor matrix
print(P)


# Multiply factor matrices
UP = np.matmul(U,P)


"""
Looking at U and P, which movie do you think will have the highest recommendation for User_3.
Multiply U and P using numpy's matmul to obtain recommendations. Call thisUP.
Complete the code to print UP.
"""

# Convert to pandas DataFrame
print (pd.DataFrame(UP, columns = P.columns, index = U.index))