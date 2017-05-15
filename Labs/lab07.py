#Lab Exercise 07
#List and Tuple Sorting

file = open("scores.txt", "r")
name=""
people=[]
first=True
for line in file:
    line=line.strip()
    name=(line[:21])
    nums=line[21:]
    nums=nums.split(" ")
    first=True 
    for x in nums:
        if x and first:
            exam1=int(x)
            first=False
        elif x:
            exam2=int(x)
    avg=(exam1+exam2)/2
    tup=name,exam1,exam2,avg
    people.append(tup)
people.sort()
total1,total2=0,0
print('{:<20s}{:>0s}{:>10s}{:>16s}'\
          .format("Name","Exam 1","Exam 2","Exam Average"))
for x in people:
    total1+=x[1]
    total2+=x[2]
    print('{:<20s}{:<11d}{:<10d}{:<16.1f}'\
          .format(x[0],x[1],x[2],x[3]))     
avg1=total1/5
avg2=total2/5
print()
print('{:<20s}{:<.1f}'\
      .format("Exam 1 Average: ",avg1))
print('{:<20s}{:<.1f}'\
      .format("Exam 2 Average: ",avg2))    