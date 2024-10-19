import numpy as np
# compute the size pf matrix
matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
matrix_size = matrix.size
#get the size/length of particular row and column
num_rows,num_cols=matrix.shape
row_length = len(matrix[ : ])
#length of first row 
col_length = len(matrix[ : ])
#length of second column
#store matrix data to a text file
matrix_to_store = np.array([[10,20,30],[40,50,60],[70,80,90]])
np.savetxt("matrix_data.txt",matrix_to_store)
#finding out variable & their features in the current scope
 
#display result
print("size of the matrix",matrix_size)
print("number of rows",num_rows)
print("number of columns",num_cols)
print("length of first row: ",row_length)
print("length of the second columns: ",col_length)
