#-----Quadratic equation--------
import cmath
import numpy as np

def quadE():
    a = 1
    b = 4
    c = 5

    # calculate the discriminant
    d = (b**2) - (4*a*c)
    #roots
    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)

    print("\nThe solution are {0} and {1}".format(root1,root2))

#----Long Division----
def longDiv():
    x = np.array([2, 3, 5, 2])
    y = np.array([2, 2, 1])
    solution = np.polydiv(x, y)

    print("\nThe solution is {0}".format(solution))

if __name__ == "__main__":
    quadE()

    longDiv()

