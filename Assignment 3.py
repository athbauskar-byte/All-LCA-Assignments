a=int(input("First side:"))
b=int(input("Second side:"))
c=int(input("Third side:"))

def is_rightangled_triangle(x,y,z):
    if x**2+y**2==z**2 or x**2+z**2==y**2 or z**2+y**2==x**2:
        print("This is a right angled traingle")
    else:
        print("This is not right angled triangle")
        
is_rightangled_triangle(a,b,c)
        
    