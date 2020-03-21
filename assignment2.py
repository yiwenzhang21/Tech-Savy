#ax**2+bx+c=0
import math
def quadratic(a,b,c):
    d = b**2-4*a*c
    if d < 0:
        x1 = x2 = "no answer" #since the graph of quadratic formula is 
    elif d == 0:
        x1 = x2 = -b/(2*a)
    else:
        x1 = ((-b + math.sqrt(d))/(2*a))
        x2 = ((-b - math.sqrt(d))/(2*a))
    return x1,x2

x1,x2 = quadratic(1,2,2)
print("x1=",x1,"x2=",x2)

x1,x2 = quadratic(1,2,1)
print("x1=",x1,"x2=",x2)

x1,x2 = quadratic(1,4,-21)
print("x1=",x1,"x2=",x2)

    