import math 
def solve_quadratic(a,b,c): 
        if ((b*b-4*a*c)<0):
            return None
        x1 = (-b + math.sqrt(b*b-4*a*c))/2*a
        x2 = (-b - math.sqrt(b*b-4*a*c))/2*a
        if ((b*b-4*a*c)>0) and (x1!=x2): 
            return (x1,x2)      
        else: 
            return (x2) 