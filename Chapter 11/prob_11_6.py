'''(Algebra: multiply two matrices) Write a function to multiply two matrices. The
header of the function is:
def multiplyMatrix(a, b)
To multiply matrix a by matrix b, the number of columns in a must be the same as
the number of rows in b, and the two matrices must have elements of the same or
compatible types. Let c be the result of the multiplication. Assume the column size
of matrix a is n.
'''

l1 = [[1,3,4],[7,11,9],[4,15,13]]
l2 = [[3,6,9],[12,55,12],[4,22,14]]


def multiplyMatrix(a,b):
     lresult =[]
     
     for i in range (len(a)):
          lresult.append([])
          for j in range(len(a)):
               c = 0
               for k in range(len(b)): ## calculating C(ij)
                    c += a[i][k] * b[k][j]

               lresult[i].append(c) ## And storing it the list

     return lresult

a = multiplyMatrix(l1,l2)
print(a)
