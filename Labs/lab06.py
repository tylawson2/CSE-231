

file=open("data.txt", "r")

name=""
height,weight,bmi=0,0,0
totalH,totalW,totalB=0,0,0
avgW,avgH,avgB=0,0,0
maxH,maxW,maxB=0,0,0
minH,minW,minB=100000,10000000,1000000
i=0
file.readline()
print("Name        Height(m)   Weight(kg)   BMI")
for line in file:
    
    line=line.strip()
    name=line[:12]
    height=float(line[12:16])
    weight=float(line[24:29])
    bmi=weight/height**2
    print('{:<s}{:>0.2f}{:>13.2f}{:>12.2f}'\
          .format(name,height,weight,bmi))
    if height>= maxH:
        maxH=height
    if height<=minH:
        minH=height
    if weight>=maxW:
        maxW=weight
    if weight<=minW:
        minW=weight
    if bmi>=maxB:
        maxB=bmi
    if bmi<=minB:
        minB=bmi
    totalH+=height
    totalW+=weight
    totalB+=bmi
    i+=1

print()
avgW=totalW/i
avgH=totalH/i
avgB=totalB/i
print('{:<12s}{:>0.2f}{:>13.2f}{:>12.2f}'\
          .format("Average",avgH,avgW,avgB))
print('{:<12s}{:>0.2f}{:>13.2f}{:>12.2f}'\
          .format("Max",maxH,maxW,maxB))
print('{:<12s}{:>0.2f}{:>13.2f}{:>12.2f}'\
          .format("Min",minH,minW,minB))
               

    
    
    
        