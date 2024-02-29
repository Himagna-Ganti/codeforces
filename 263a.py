
from sys import stdin,stdout





def solve(array):
    
    
    for i in range(len(array)):
        for j in range(len(array[i])):
            if array[i][j]=='1':
                
                stdout.write(str(abs(i-2)+(abs(j-4))//2))
    pass

def main():
    
    
    array=[]
    for line in stdin.readlines():
        array.append(line.strip('\n'))
    solve(array)
        
if __name__ == "__main__":
    main()