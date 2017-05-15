    ###########################################################
    #  Computer Project #1
    #
    #  Algorithm
    #    prompt for an number of rods
    #    input an integer
    #    convert rods to Meters, Feet, Miles, Furlongs, and Minutes to walk 
    #    the distance in rods
    #    Print all conversions
    ###########################################################

num_str1 = input('Input rods: ')  #prompt user the input a number of rods
numRods = float(num_str1) #convert string response to a float
print('You input ',numRods,' rods.') 
    #Tell the user how many rods he chose to input
    
meters=(numRods*5.0292) #Convert Rods to Meters
feet=(numRods*16.5) #Convert rods to feet
miles=(feet/5280) #Convert rods to miles
furlongs=(numRods/40) #convert rods to furlongs
minutes=(miles/3.1)*(60) #calculates minutes to walk the given amount of rods

print()#add a blank line to space it out and to make it look pretty
print("Conversions") 
    #Writes out the word converions in order to label the conversions
print("Meters:",meters,) #print the meters
print("Feet:",feet,) #print the feet
print("Miles:",miles,) #print the miles
print("Furlongs:",furlongs,) #print the furlongs
print("Minutes to walk" ,numRods, "rods:" ,minutes,) 
    #print the time to walk the given number of rods