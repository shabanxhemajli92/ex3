# Task 1
for i in range(0,3):
    n= input("give me a number:")
    if int(n) % 2==0:
        print("even number")
    else:
        print("it is odd")     

# Task 2
n=input("How many arguments you want to use: ")
start=input("Enter the number needed to start: ")
stop=input("This is the point to where everything stops!")
step=input("How many numbers do you want to count up in a step: ")
for i in range(start,stop,step):
    print(i)
              
        