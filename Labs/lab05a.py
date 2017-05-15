#Lab 5 Part 1
#finds words in dictionary.txt that have one s, one vowel, all lowercase,
#and length of 7 letters

vowels="aeiouy"

file=open("dictionary.txt", "r")

for line in file:
    x=0
    line=line.strip()
    if (len(line)!=7):
        continue
    if not line.islower():
        continue
    if "s" in line:
        continue
    for i in range(len(line)):
        if line[i] in vowels:
            x+=1
    if x!=1:
        continue
    print(line)

file.close