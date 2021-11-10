import math 
def solve_quadratic(a,b,c): 
        y = b*b-4*a*c 
        if (y< 0):
            return None
        x1 = (-b + math.sqrt(y))/2*a
        x2 = (-b - math.sqrt(y))/2*a
        if (y>0) and (x1!=x2): 
            return (x1,x2)      
        else: 
            return (x2) 