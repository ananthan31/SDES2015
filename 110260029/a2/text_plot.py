import math

def __findrange(a,b):
    return float(a-b)

def __createline(l,column):
    if len(l)==0:
        return ' '*column
    else:
        length=len(l)
        line=' '*l[0]+'*'
        for i in range(1,length):
            extra=' '*(l[i]-l[i-1]-1)
            line+=extra+'*'
        line+=' '*(column-l[-1]-1)
        return line
    
def __find_any_y_in_line(line,ya,y):
    all_yindex=[]
    if line==0:
        for i in range(len(y)):
            if y[i]<=ya[line]:
                all_yindex.append(i)
    else:
        for i in range(len(y)):
            if y[i]>ya[line-1] and y[i]<=ya[line]:
                all_yindex.append(i)
    return all_yindex

def __find_all_x_for_y(all_yindex, xa, x):
    all_xindex=[]
    for i in all_yindex:
        tocheck=x[i]
        for j in range(len(xa)):
            if j==0:
                if tocheck<=xa[j]:
                    all_xindex.append(j)
            else:
                if tocheck>xa[j-1] and tocheck<=xa[j]:
                    all_xindex.append(j)
    all_xindex_without_duplicates=__unique(all_xindex)
    all_xindex_without_duplicates.sort()                
    return all_xindex_without_duplicates

def __unique(x):
    x_without_dup=[]
    for i in x:
        if i not in x_without_dup:
            x_without_dup.append(i)
    return x_without_dup
    

def plot(x,yold):
    if len(x)!=len(yold):
        return
    
    row=30
    column=80
    
    xa=[]
    ya=[]
    y=[]
    
    for i in range(0,len(yold)):
        y.append(row-yold[i])
    
    min_x=min(x)
    max_x=max(x)
    min_y=min(y)
    max_y=max(y)
    
    x_range=__findrange(max_x,min_x)
    y_range=__findrange(max_y,min_y)
    
    xa_ivl=x_range/column
    ya_ivl=y_range/row
    
    for i in range(1,column+1):
        xa.append(min_x+i*xa_ivl)
    
    for i in range(1,row+1):
        ya.append(min_y+i*ya_ivl)
    
    for line in range(row):
        all_yindex=__find_any_y_in_line(line,ya,y)
        all_xindex=__find_all_x_for_y(all_yindex, xa, x)
        print __createline(all_xindex,column)

if __name__=="__main__":
    x=[]
    y=[]
    interval=50
    increment=2*math.pi/interval
    for i in range(interval+1):
        x.append(i*increment)
        y.append(math.sin(i*increment))
    plot(x,y)
