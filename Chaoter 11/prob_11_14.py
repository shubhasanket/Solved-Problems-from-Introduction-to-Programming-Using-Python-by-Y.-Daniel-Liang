'''**11.14 (Explore matrix) Write a program that prompts the user to enter the length of a
square matrix, randomly fills in 0s and 1s into the matrix, prints the matrix, and
finds the rows, columns, and major diagonal with all 0s or all 1s.
'''
import random

def main():
     n = eval(input("Enter the size of the matrix: "))
     ## Create a random matrix with the given size
     l = []
     for i in range(n):
          l.append([])
          
          for j in range(n):
               l[i].append(random.randint(0,1))
               
     ## Create 3 lists. 1 for row, column and major diagonals respectively
     lr = []
     lc = []
     ld =[]
     maj_dia_leftToright = 0 ## Creating variables to compute the sum of the diagonals
     maj_dia_rightToleft = 0
     
     for i in range(n):
          ## Checking for the rows
          if sum(l[i]) == n: ## If the all the elements of the rows == 1
               doTheNeedful(lr, i, 1)

               
          elif sum(l[i]) == 0: ## If the all the elements of the rows == 0
               doTheNeedful(lr, i, 0)

          ## Checking for the columns
          s = 0
          for j in range (n): ## Calculating the sum of the elements in the column
               s += l[j][i]

          if s == n: ## If the all the elements of the column == 1
               doTheNeedful(lc, i, 1)


          elif s == 0: ## If the all the elements of the column == 0
               doTheNeedful(lc, i, 0)

          maj_dia_leftToright += l[i][i] ## Summing diagonal 1
          maj_dia_rightToleft += l[i][n-1-i] ## Summing diagonal 2

     ## Printing the matrix
     for i in range (n):
          
          print("".join(str(l[i])))

     ## Printing the results for rows
     if len(lr) == 0:
          print("No same numbers in a row")
     else:
          for k in range (len(lr)):
               print("All", str(lr[k][1]) + "s in row " + str(lr[k][0]))
               

     ## Printing the results for columns
     if len(lc) == 0:
          print("No same numbers in a column")
     else:
          for m in range (len(lc)):
               print("All", str(lc[m][1]) + "s in column " + str(lc[m][0]))

     ## Printing the results of the diagonals
     dia_check = False
     
     if maj_dia_leftToright == n: ## Checking if this dia has all 1s
          dia_check = True
          print("All 1s in major diagonal (top left to bottom right)")
     elif maj_dia_leftToright == 0: ## Checking if it has all 0s
          dia_check = True
          print("All 0s in major diagonal (top left to bottom right)")

     if maj_dia_rightToleft == n: ## Repeating the previous process for the second diagonal
          dia_check = True
          print("All 1s in major diagonal (top right to bottom left)")
     elif maj_dia_rightToleft== 0:
          dia_check = True
          print("All 0s in major diagonal (top right to bottom left)")

     if not dia_check: 
          print("No same numbers in major diagonals")

          

def doTheNeedful(m, index, oneOrzero): ## This routine appends sub lists to master lists, and stores the column/row number and the common element (0 or 1)

          m.append([])
          m[len(m)-1].append(index)
          m[len(m)-1].append(oneOrzero)



main()









               
               
