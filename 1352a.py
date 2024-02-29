
from sys import stdin,stdout





def solve(a):
    
    res=[]
    n=len(a)
    summ=-0

    for i,c in enumerate(a):
        if c=='0':
            continue
        else:
            res.append(c+((n-1-i)*'0'))
            summ+=1
    stdout.write(str(summ)+'\n')
    stdout.write(' '.join(res)+'\n')


    pass

def main():
    
    n=stdin.readline()
    array=[]
    for line in stdin.readlines():
        array.append(line.strip('\n'))
    
    for a in array:
        if a:
            solve(a)
        
if __name__ == "__main__":
    main()