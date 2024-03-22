'''(Sum elements column by column) Write a function that returns the sum of all the
elements in a specified column in a matrix using the following header:
def sumColumn(m, columnIndex):
Write a test program that reads a matrix and displays the sum of each column
'''

def sumColumn(m, columnIndex):
     s = 0
     for i in range (len(m)):
          s += m[i][columnIndex]
     return s

def main():
     l = [[1,2,3,4], [2,3,4,2], [8,4,9,6], [13,56,12,11], [12,23,45,12]]

     for i in range(len(l[0])):
          s = sumColumn(l, i)
          print("The sum of the column", str(i), "is", s)

main()
          
