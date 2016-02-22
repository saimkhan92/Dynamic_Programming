# Given a matrix of dimensions m x n having all entries as 1 or 0, find out the size of maximum size square sub-matrix with all 1s. 

matrix=[[1,0,0,1,1,1],[1,0,0,1,1,1],[1,0,0,1,1,1],[1,1,0,1,0,1],[0,0,0,1,0,1],[1,0,0,1,1,1]]
testmatrix=matrix
for i in matrix:
    print(i)
print("\n")


rows=len(matrix)
columns=len(matrix[0])

for i in range(rows):
    for j in range(columns):
        if i==0 or j==0:
            testmatrix[i][j]=matrix[i][j]
        elif matrix[i][j]==0:
            testmatrix[i][j]=0
        else:
            testmatrix[i][j]=min(matrix[i-1][j],matrix[i][j-1],matrix[i-1][j-1])+1

for i in testmatrix:
    print(i)            

p=0

for i in range(rows):
    for j in range(columns):
        if testmatrix[i][j]>p:
            p=testmatrix[i][j]

print("The maximum size square sub-matrix with all 1s is {}".format(p))
