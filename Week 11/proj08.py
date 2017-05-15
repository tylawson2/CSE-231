###################################
#     Computer Project #8
#
#     United States Data Charts
#        Prompt for a file
#        Prompt for a region
#        Show statistics
#        ask if user wants graph
#        if yes, ask for x and y:
#        show Graph
####################################


#import sys
#def input( prompt=None ):
#    if prompt != None:
#        print( prompt, end="" )
#    aaa_str = sys.stdin.readline()
#    aaa_str = aaa_str.rstrip( "\n" )
#    print( aaa_str )
#    return aaa_str
    
import pylab

# Here are some constants that are optional to use -- feel free to modify them, if you wish
REGION_LIST = ['far_west',
 'great_lakes',
 'mideast',
 'new_england',
 'plains',
 'rocky_mountain',
 'southeast',
 'southwest',
 'all']
VALUES_LIST = ['Pop', 'GDP', 'PI', 'Sub', 'CE', 'TPI', 'GDPp', 'PIp']
VALUES_NAMES = ['State','Population(m)','GDP(b)','Income(b)','Subsidies(m)','Compensation(b)','Taxes(b)','GDP per capita','Income per capita']
PROMPT1 = "Specify a region from this list -- far_west,great_lakes,mideast,new_england,plains,rocky_mountain,southeast,southwest,all: "
PROMPT2 = "Specify x and y values, space separated from Pop, GDP, PI, Sub, CE, TPI, GDPp, PIp: "

def plot_regression(x,y):
    '''Draws a regression line for values in lists x and y.
       x and y must be the same length.'''
    xarr = pylab.array(x) #numpy array
    yarr = pylab.array(y) #numpy arry
    m,b = pylab.polyfit(xarr,yarr, deg = 1) #creates line, only takes numpy arrays
    #as parameters
    pylab.plot(xarr,m*xarr + b, '-') #plotting the regression line

def open_file():
    '''prompt user and open a file'''
    go=True
    while go:
        file=input("Enter a filename: ")#ask for file
        try:
            file=open(file,"r")#try to open it
            go=False
        except:
            print("Error in filename.")#account for errors
            go=True
    return file
    
def read_file(fp):
    '''read the file and make dictionaries'''
    go=True
    while go:
        region=input(PROMPT1)#ask for file
        dic={}
        if region.lower() in REGION_LIST:
                #check to make sure it is a valid region
            region=REGION_LIST[REGION_LIST.index(region.lower())]
            fp.readline()#skip first line
            if region.lower()=="all":#do all regions
                for line in fp:
                    line=line.strip().split(',')#seperate numbers 
                    q=float(line[3])*1000
                    r=float(line[4])*1000#get new variables
                    s=float(line[2])
                    gdpp=q/s
                    icp=r/s
                    line.append(gdpp)
                    line.append(icp)
                    key=line.pop(0)#add to dictionary
                    dic[key]=line
            else:
                for line in fp:#for specific region create dictionary
                    line=line.strip().split(',')
                    if line[1].lower()==region.lower():
                        q=float(line[3])*1000
                        r=float(line[4])*1000
                        s=float(line[2])
                        gdpp=q/s
                        icp=r/s
                        line.append(gdpp)
                        line.append(icp)
                        key=line.pop(0)
                        dic[key]=line
            go=False
        else:
            print("Error in Region.")#account for errors
            go=True
    return dic,region

def display_states(dic,region):
    '''display the state data'''
    max1=0
    max2=0
    min1=100000000000#variables 
    min2=1000000000
    print("\nData for the ",region," region:\n")#tell the data being used
    for i in dic.values():
        if float(i[7])>=float(max1):
            max1=i[7]
        if float(i[8])>=float(max2):#find maxes and mins
            max2=i[8]
        if float(i[7])<=float(min1):
            min1=i[7]
        if float(i[8])<=float(min2):
            min2=i[8]
    for i in dic:#show first max
        if max1==dic[i][7]:
            print(i," has the highest GDP per capita at "'${:,.2f}'\
                  .format(max1))
    for i in dic:
        if min1==dic[i][7]:#show first min
            print(i," has the lowest GDP per capita at "'${:,.2f}'\
                  .format(min1))
            print()
    for i in dic:#show other maxes and mins
        if max2==dic[i][8]:
            print(i," has the highest ICP per capita at "'${:,.2f}'\
                  .format(max2))
    for i in dic:
        if min2==dic[i][8]:
            print(i," has the lowest ICP per capita at "'${:,.2f}'\
                  .format(min2))
            print()
     #print data chart
    print("Data for all states in the ",region," region\n")
    print('{:<15}{:>10s}{:>10s}{:>13s}{:>17s}{:>18s}{:>20s}{:>20s}{:>20s}'\
          .format('State','Population(m)','GDP(b)','Income(b)','Subsidies(m)',\
                  'Compensation(b)','Taxes(b)','GDP per capita',\
                  'Income per capita'))
    #sort it
    alist=sorted(list(dic))
    #print it
    for i in alist:
        print('{:<15s}{:>13,.2f}{:>10,.2f}{:>13,.2f}{:>17,.2f}{:>18,.2f}\
              {:>6,.2f}{:>20,.2f}{:>20,.2f}'.format(i,float(dic[i][1]),\
              float(dic[i][2]),float(dic[i][3]),float(dic[i][4]),float\
              (dic[i][5]),float(dic[i][6]),float(dic[i][7]),float(dic[i][8])))
    
def plot(dic):   # you need to replace pass with parameters
    '''Plot the values in the parameters.'''
    #pass # placeholder
    
    # prompt for which values to plot; these will be the x and y
    go=True
    while go:
        stuff=input(PROMPT2).split()#
        go=False
        for i in stuff:
            if i not in VALUES_LIST:
                go=True
                print("Error")
            
    
    xname=stuff[0]
    yname=stuff[1]
    q=VALUES_LIST.index(xname)+1
    r=VALUES_LIST.index(yname)+1
    x=[]
    y=[]
    for u in dic.values():
        x.append(float(u[q]))
        y.append(float(u[r]))
   
    # build x, the list of x values
    # build y, the list of y values
    # hint: list comprehension is a slick way to build x and y

    # In the following you need to replace 'pass' with your own arguments
    str1='{} {} {}'.format(xname,"vs.",yname)
    pylab.title(str1)   # plot title

    pylab.xlabel(xname)   #label x axis
    pylab.ylabel(yname)   #label y axis
    
    pylab.scatter(x,y)
    for i, txt in enumerate(dic.keys()): 
        pylab.annotate(txt, (x[i],y[i]))
    plot_regression(x,y)
   
    # USE ONLY ONE OF THESE TWO
    pylab.show()                # displays the plot      
    #pylab.savefig("plot.png")   # saves the plot to file plot.png
    

def main():
    fp=open_file()
    tup1=read_file(fp)
    dic=tup1[0]
    region=tup1[1]
    display_states(dic,region)
    plotA=input("Do you want to create a plot? ")
    if plotA=="yes":
        plot(dic)
    
    
if __name__ == "__main__":
    main()
    
    #Questions
#Q1: 7
#Q2: 2
#Q3: 1
#Q4: 6
#Q5: 7