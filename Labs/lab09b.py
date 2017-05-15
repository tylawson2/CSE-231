def read(file):
    dictb={}
    for line in file:
        line=line.strip()
        line=line.split()
        if line[0]!="Name":
            dictb[line[0]]=(line[1])
        
    return dictb

def output(dicta,key):
    
    print('{:10s}{:5s}'.format("Name","Total"))
    for i in key:
       
        print('{:7s}{:5d}'.format(i,dicta[i]))

  
def main():
    file1=open("data1.txt", "r")
    file2=open("data2.txt", "r")
    dict1=read(file1)
    dict2=read(file2)
    dictf={}
    for i in (dict1):
        
        if i in dict2:
            dictf[i] =(int(dict1[i])+int(dict2[i]))
        else:
            dictf[i]=(int(dict1[i]))
    for i in dict2:
        if i not in dictf:
            dictf[i]=(int(dict2[i]))
    key=sorted(dictf)
    output(dictf,key)
    file1.close()
    file2.close()
    
main()