"""
Non-Negative Matrix Factorization
It's possible for one matrix to have two equally close factorizations where one has all positive values, and the other has some negative values. The matrix M has been factored twice using two different factorizations. Take a look at each pair of factor matrices L and U, and W and H to see the differences. Then use their products to see that they produce essentially the same product.

Instructions
100 XP
Use the print command to view the L and U matrices. Notice that some values in matrices L and U are negative.
Use the print command to view the W and H matrices. Notice that all values in these two matrices are positive.
The L andU matrices and W and H matrices have been multiplied together to produce the LU and WH matrices respectively. Use the getRMSE(product_matrix, original_matrix) function to see how close LU is to M compared to how close WH is to M. Are they similar?
"""



# View the L, U, W, and H matrices.
print("Matrices L and U:") 
print(L)
print(U)

print("Matrices W and H:")
print(W)
print(H)

# Calculate RMSE between LU and M
print ("RMSE of LU: ", getRMSE(LU, M))

# Calculate RMSE between WH and M
print ("RMSE of WH: ", getRMSE(WH, M))