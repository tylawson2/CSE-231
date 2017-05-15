#Lab Exercise #4
#Functions

def squares(a,b):
    sum=0
    for i in range(b):
       sum+=a**2
       a+=1
    return sum

def cubes(a,b):
    sum=0
    for i in range(b):
        sum+=a**3
        a+=1
    return sum

go=True

while go:
    
    command= input("\nEnter a command: squares, cubes, or exit-- ")
    command=command.lower()
    if(command=="exit" or command=="squares" or command=="cubes"):
        if(command=="exit"):
            go=False
            print("\nProgram halted normally")
            
        if(command=="squares"):
            num1=int(input("What will be your initial integer? "))
            num2=int(input("How many numbers will you use? "))
            theSum=squares(num1,num2)
            print("The sum of your function is: ",theSum,)
            
        if(command=="cubes"):
            num1=int(input("What will be your initial integer? "))
            num2=int(input("How many numbers will you use? "))
            theSum=squares(num1,num2)
            print("The sum of your function is: ",theSum,)
    else:
        print("\n*** Invalid choice ***")
    
    
    