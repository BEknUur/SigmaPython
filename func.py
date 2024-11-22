import math
def plus(a,b):
    print(a+b) #12+(-1)=11

def minus(a,b):
    print(math.fabs(a-b))     #a-- +


def divide(a,b):
    if(a>=b):
        if(b==0):
            print("Nolge bolyge bolmaidy")
        else:
            print(a/b)
    elif(a<b):
        if(a==0):
            print("Nolge bolyge bolmaidy")
        else:
            print(b/a)

def multi(a,b):
    print(a*b)
 

a=int(input("First san:"))
b=int(input("Second san:"))
print("Kosindi eseptey:")
plus(a,b)
print("Azaityndi eseptey:")
minus(a,b)
print("Bolindi eseptey:")
divide(a,b)
print("Kobeitindi eseptey:")
multi(a,b)