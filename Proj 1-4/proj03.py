###################################
#
#   Project #3: Change Making Program
#   
#       Greedy Algorith
#         Recieve a price 
#         Recieve amount paid
#         Calculate change to give in coins and keep track of coins
#         end when out of change or told to stop
#         give user his/her results
#
#
####################################


print()
print("Welcome to the change-making program.")
val= input("\nEnter the purchase price (xx.xx) or `q' to quit: ")
    #Get initial value
numVal= float(val)#convert value to a usuable float
total=410#give all variables initial values

change=0
Q=10
x=0
y=0
z=0
m=0
D=10
N=10
P=10
save=0
t=0
paying=True
end=False

while not (val=="q")and not end:#run program while conditions are true
    numVal= float(val)
    paying=True
    if (numVal<0):#check if the number is negative
        print("\nError: purchase price must be non-negative.")

    else:#run the program to make change
        while paying:
            paid=float(input("\nInput dollars paid (int): "))
                #get input for money given to pay
            print()
            if(paid>=numVal):#check if paid more than cost
                change=paid-numVal#reassign value to change once paid
                t=change
                change*=100
                save=change
                    
                if(change<=total):#check if you have enough change
                    total-=change
                    if(Q>0):#get amount of quarters used
                        x=int(change//25)
                        Q-=x
                        if(Q<0):
                            change%=25
                            change-=Q*25
                            x+=Q
                            Q-=Q
                        else:
                            change%=25
                    
                    if(D>0):#get amount of dimes used        
                        y=int(change//10)
                        D-=y
                        if(D<0):
                            change%=10
                            change-=D*10
                            y+=D
                            D-=D
                        else:
                            change%=10
                
                    if(N>0): #gets amount of nickels used       
                        z=int(change//5)
                        N-=z
                        if(N<0):
                            change%=5
                            change-=N*5
                            z+=N
                            N-=N
                        else:
                            change%=5
                    
                    if(P>0):   #gets amount of pennies used
                        change=int(round(change, 1))
                        m=int(change//1)
                        P-=m
                        if(P<0):
                            change%=1
                            change-=P
                            m+=P
                            P-=P
                        else:
                            change%=1
                            
                    if(save==0):
                        print("\nNo change")
                        
                    else:
                        print("Collect payment below:")#print out the change
                        print("Change needed: ","%.2f" % round(t,2),)
                        if(x>0):
                            print("Quarters: ",x,)
                        if(y>0):
                            print("Dimes: ",y,)
                        if(z>0):
                            print("Nickels: ",z,)
                        if(m>0):
                            print("Pennies: ",m,)
                            
                    print("Stock: ",Q,"quarters, ",D," dimes, ",N," nickels, "\
                    "and ",P," pennies")#print out inventory
        
                else:#tell the user there is not enough change
                    print("\nError: ran out of coins.")
                  
                    end=True
                paying=False
            else:#tell the user they did not pay enough
                print("\nError: insufficient payment.")
    if not end:#if still runinning get a new value for the next item            
        val= input("\nEnter the purchase price (xx.xx) or `q' to quit: ")


print()#tell what is left for change if ended with q
print("Remaining change: ","%.2f" % round(total/100,2),)  


#Questions
#Q1: 6
#Q2: 2
#Q3: 1
#Q4: 6
#Q5: 7