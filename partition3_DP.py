import sys

table=[]
S=[]

'''
function to find out if a list of integers are 3-partionable i.e.
the list of integers can be subdivided to 3 disjoint subsets with
sums same. i.e. sum of the integers in each subset = sum of all integers / 3

Logic:
    Using recursion with dynamic programmimg.
    sum of all integers /3 should be an integer = the sum of each partition
      - if not integer, directly marked as not partionable
    The maximum integer in the set should be <= the sum of all integers in set/3
      - if max(S) > sum(S)/3, S is not 3 partitionable, because max(S) can't be put in any oartition
    
    Dynamic programming table[i][j] stores 1 if it is possible to create a sum of i in one partition and sum of j in other partition,
     size of table is sum(S)/3+1 to store sums of 0,1,... upto sum(S)/3.
     After filling up the table recursively, if table[3][3] is 1, then S is 3 partitionable

    Base case:
     table[0][0]=1, as both partitions can be empty
    recursion:
     For all integer s in set S, check each row i and columns i to end of row.
     If table[i][j] is set to 1, then integer s can be put in either bucket, so table[i+s][j] and table[i][j+s] will be made 1
        since we are filling up only one side of diagonal, while filling up table[i][j], check if j<i, then fill up table[j][i] instead.
        if i or j > sum(S)/3, no need to fill up
    Once all integers are read, check value of last column and row of table.
     1 : S is 3 partionable
     0 : S is NOT 3 partionable 
    
'''
def canPartition3():

    global S,table

    # fail conditions check
    pSize=sum(S)/3
    if pSize!=int(pSize) or max(S)>pSize:
        return False

    # table initialisation
    pSize=int(pSize)
    table=[[False for _ in range(pSize +1)] for _ in range(pSize +1)]

    # base case
    table[0][0]=True

    m=0
    # recursion
    for i in range(len(S)):
        m += S[i]           # maximum sum possible with integers in set S upto i
        r=min(m,pSize)+1    # iterate till r -> minimum of sum possible and end of row
        for row in range(r):
            for col in range(row,r):
                if table[row][col]==True:
                    if row+S[i] <= pSize:      # since row < col always, row+S[i] > pSize implies col also out of range
                        table[row+S[i]][col]=True
                    if col+S[i] <= pSize:
                        if col+S[i] >= row:
                            table[row][col+S[i]]=True
                        else:
                            table[col+S[i]][row]=True
    return table[-1][-1]

'''
functions for testing
'''
def setdata(data):
    global S
    S=data
    return canPartition3()

def testit():

    if setdata([3,3,3])==True: print('ok')
    else: print('not ok')
    if setdata([1,2,3,4])==False: print('ok')
    else: print('not ok')
    if setdata([3,3,3,25])==False: print('ok')
    else: print('not ok')
    if setdata([1,2,3,4,4,5,8])==True: print('ok')
    else: print('not ok')
    if setdata([2,2,3,5])==False: print('ok')
    else: print('not ok')
    
    
    
if __name__=='__main__':

    #testit()  # uncomment this line, and comment rest of the lines, for testing
    
    try:
        S=list(map(int,input("Enter integers:").split()))
    except:
        sys.exit('Enter only integers, seperated by spaces, e.g. 1 2 3')

    if canPartition3()==True:
        print("partionable")
    else:
        print("Not partionable")
