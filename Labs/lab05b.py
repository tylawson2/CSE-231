#Lab 5 Part 2
#finds words in dictionary.txt that have "aeiou" in order

vowels="aeiou"
file=open("dictionary.txt", "r")
x=0
for line in file:
    
    line=line.strip()
    right=""
    for i in range(len(line)):
        if line[i] in vowels:
            right+=line[i]
    
    if(right==vowels):
        x+=1
        print(x,") ",line)

file.close