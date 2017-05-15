#lab exercise 8
#Benford's Law

nums={1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
bens={1:"(30.1%)",2:"(17.6%)",3:"(12.5%)",4:"( 9.7%)",5:"( 7.9%)",6:"( 6.7%)",\
      7:"( 5.8%)",8:"( 4.1%)",9:"( 4.6%)"}

def main():
    total=0
    file=open_file()
    for line in file:
        stuff=line.strip()
        for i in stuff:
            #print(i)
            if i.isdigit() and i!='0':
                nums[int(i)]+=1
                total+=1
                break
    file.close()
    print("\n"'{:<6s}{:<8s}{:<7s}'.format("Digit","Percent","Benford"))
    for j in nums:
        nums[j]=(nums[j]/total)*100
        print('{:>4d}:{:>6.1f}%{:>10s}'.format(j,nums[j],bens[j]))
        
def open_file():
    '''prompts user for file name until it works then returns pointer'''
    b=True
    while b: 
        s=input("Enter file name: ")
        try:
            file= open(s,"r")
            b=False
        except:
            continue
    return file
main()