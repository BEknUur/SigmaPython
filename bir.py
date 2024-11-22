from array import array # array-массив
N=int(input())
A=array("i")
Sum=0  # Sum=3
A=[0]*N 
for i in range(0,N):  # i=0   sum=1   i=1 sum=1+2=3   i=2  3+3=6
    A[i]=int(input())
    if(A[i]<=0 and A[i]%2==0):
        Sum+=A[i]
    else:
        print("It is not our number")


print(Sum)


#  Тақ жанеде теріс емес сандардың қосыныдысын табу қажет  >=0:  
# Жұп жане теріс сандардың қосындысын табу қажет!