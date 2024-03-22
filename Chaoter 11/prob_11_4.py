'''(Compute the weekly hours for each employee) Suppose the weekly hours for all
employees are stored in a table. Each row records an employee’s seven-day work
hours with seven columns. For example, the following table stores the work hours
for eight employees. Write a program that displays employees and their total hours
in decreasing order of the total hours.
'''

l = [[2, 4, 3, 4, 5, 8, 8],
     [7, 3, 4, 3, 3, 4, 4],
     [3, 3, 4, 3, 3, 2, 2],
     [9, 3, 4, 7, 3, 4, 1],
     [3, 5, 4, 3, 6, 3, 8],
     [3, 4, 4, 6, 3, 4, 4],
     [3, 7, 4, 8, 3, 8, 4],
     [6, 3, 5, 9, 2, 7, 9]]

def totalWorkHours(m):
     newl = []
     for i in range (len(l)):
          newl.append([]) ## Creating lists with length == 2
          newl[i].append(sum(m[i])) ## The total number hours is the first element
          newl[i].append(i) ## Adding the number of the employee. For example: if it is employee no. 0, 0 is added as the second element of the list  

     newl.sort() ## The elements of the sublists are stored in that particular order to help us use the sort() routine
     newl.reverse()## The list is reversed so that we have the working hours in descending order
     print("The employees and their total work hours in descending order is given below")

     for j in range (len(l)): ## The result is printed
          print("Employee " + str(newl[j][1]) + " works for", str(newl[j][0]), "hours")

totalWorkHours(l)

     
