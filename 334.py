a=int(input())
b=int(input())
c=int(input())
d=int(input())
sigma=[]
for i in range(a,b+1):
    if(i%d==c):
        sigma.append(i)
        print (i,end='')    

for i in range(len(sigma)):
    print (sigma[i],end=' ')

    '''
    print(i)
    2
    3
    4
    5

    print(i,end=' ' )
    2 3 4 5 

    
    
    '''
        
  