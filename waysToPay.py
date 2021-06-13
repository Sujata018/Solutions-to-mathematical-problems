import sys
import numpy

dp=[]             # global matrix for dynamic programming
c=[]              # array storing denominations of coins available

'''
Calculate number of ways to pay N rupees with coins of denominations c1,c2,...,cm,
assuming infinite supply of each types of coins 

Input : N -> rupees to pay
        c1,...,cm -> denominations of coins available
Output: Number of ways (integer)

Logic : Calculate using dynamic programming.
        if n==0,
           D(n,i)=1 # can pay 0 rupees in one way only.
        if n<ci,
           D(n,i)=D(n,i-1) # can't pay n rupees using ci
        else:
           D(n,i)=D(n,i-1)+D(n-ci,i) # way to pay n rupees not using ci + way to pay n rupees using ci 
        where D(n,i) denotes number of ways to pay n rupees using coins c1,c2 upto ci only.
'''

def findways(n,i):
    
    global dp,c

    for row in range(1,n+1):        # Fill up dynamic programmimg array for payong 0 to N rupees
        for column in range(1,i+1): # and for 1 to i coins
            if row>=c[column-1]:    # if n >= c[i]
                dp[row,column]=dp[row,column-1]+dp[row-c[column-1],column]
            else:                   # if n < c[i]
                dp[row,column]=dp[row,column-1]
        
    return dp[n,i]

'''
functions findit() and testit() are written to test the program for all test cases
by running it only once.

Process to test:
     Uncomment line '# testit() ' in the main function.
     Run the program
     A number of 'ok's should be printed at stdout, if all test cases passed.
     If some test cases are not passed, 'not ok' along with dp matrix details
        will be written to stdout.
'''
def findit(N,coins,r):
    
    global dp,c
    
    c=coins
    nc=len(c)
    dp=numpy.zeros([N+1,nc+1],dtype=int)
    dp[0,:]=1
    findways(N,nc)
    
    if dp[-1,-1]==r:
        print ('ok')
    else: 
        print ('not ok for ',N,coins,dp)
    
    
def testit():

    # to add test cases, enter new line findit(n,c,r)
    # Expected number os ways to pay n rupees, using list of coins c, is r
    findit(0,[2],1)
    findit(2,[],0)
    findit(2,[2],1)
    findit(2,[1,2],2)
    findit(3,[2],0)
    findit(3,[1,2],2)
    findit(4,[1,2,3,4],5)


if __name__=='__main__':

   # testit()  # uncomment for testing all test cases at one go
   
    try:
        N=int(input("How much to pay? :"))
    except:
        sys.exit("Enter positive integer.")
    try:
        c=list(map(int,input("Enter the available currencies, seperated by spaces :").split()))
    except:
        sys.exit("Invalid currencies. Enter positive integers like <1 2 3 4>")
    
    nc=len(c)
    dp=numpy.zeros([N+1,nc+1],dtype=int)
    dp[0,:]=1
    findways(N,nc)
    
    print ("Number of ways to pay Rupees ", N, " using coins of Rs. ", *c, " is ", dp[-1,-1]) 
