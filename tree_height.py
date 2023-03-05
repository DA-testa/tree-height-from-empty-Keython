# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    par=parents.split()
    mas=[[] for i in range(n)]
    ind=0
    for i in range(n):
        if par[i]=='-1':
            ind=i
            continue
        mas[int(par[i])].append(i)    
    max_height = 0
    maina=[[ind,1]]
    while len(maina)!=0:
        for i in mas[maina[0][0]]:
            maina.append([i,maina[0][1]+1])
        max_height=maina[0][1]
        del maina[0]

    
    # Your code here
    return max_height
    

def main():
    # implement input form keyboard and from files
    n=input()
    if n[0] == 'I':
        n=input()
        parents=input()
    else:
        f = open(n, "r")
        n=f.readline()
        parents=f.readline()
    print(compute_height(int(n),parents))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

# print(numpy.array([1,2,3]))
