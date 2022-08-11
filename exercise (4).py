''' # Task 1
from argparse import RawTextHelpFormatter


for i in range(0,3):
     n= input("give me a number:")
     if int(n) % 2==0:
         print("even number")
     else:
        print("it is odd")'''     

''' Task 2
n=input("How many arguments you want to use: ")
n=int(n)
if n>=3:
    start=input("Insert the number needed to start: ")
    stop=input("This is the point to where everything stops!")
    step=input("How many numbers do you want to count up in a step: ")
   #this will check the number of arguments,this will check for the 3 arguments(sss)
elif n==2:
    step=1
    start=input("Insert the number needed to start: ")
    stop=input("This is the point to where everything stops!")    
    #this will only check for 2 arguments
else:
    start=1
    step=1
    stop=input("This is the point to where everything stops!")
    #this will only check for 1 argument    
start=int(start)
stop=int(stop)
step=int(step)
for i in range(start,stop,step):
   print(i)'''

#Task3#   
v=int(input("Enter a number: "))
for j in range(2,v+1,1): 
#this will devide the num by two and will stop at the number above it , dividing it by every single number    
    if v % j == 0:
        print(j)
                 


