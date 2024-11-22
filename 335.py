import math
a=int(input())
b=int(input())
for i in range(a,b+1):
    if(int(math.sqrt(i))==math.sqrt(i)):
        print(i,end=' ')