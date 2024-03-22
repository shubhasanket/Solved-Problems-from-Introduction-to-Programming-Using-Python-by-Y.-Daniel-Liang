'''(Towers of Hanoi) Modify Listing 15.8, TowersOfHanoi.py, so that
the program finds the number of moves needed to move n disks from
tower A to tower B. (Hint: Use a global variable and increment
it for every move.)
'''
global x
x = 0
def main():
    n = eval(input("Enter nnumber of disks: "))
##    print("The moves are: ")
    moveDisks(n, 'A', 'B', 'C')

def moveDisks(n, fromTower, toTower, auxTower):
    global x
    x += 1
    if n == 1:
        return
##        print("Move disk", n, "from", fromTower, "to", toTower)
    else:
        moveDisks(n-1, fromTower, toTower, auxTower)
##        print("Move disks", n, "from", fromTower, "to", toTower)
        moveDisks(n-1, auxTower, toTower, fromTower)

main()
print("The function moveDisks has been invoked", x, "times")
