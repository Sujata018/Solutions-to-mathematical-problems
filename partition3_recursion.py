import sys

table=[]
N=0
S=[]

'''
function to find out if a list of integers are 3-partionable i.e.
the list of integers can be subdivided to 3 disjoint subsets with
sums same. i.e. sum of the integers in each subset = sum of all integers / 3

Logic:
    With recursion.
    S(sum/3,sum/3,sum/3,1)=1st integer is included in 1st division|2nd division|3rd division
      =S(sum/3-int1,sum/3,sum/3,2)|S(sum/3-int1,sum/3,sum/3,2)|S(sum/3-int1,sum/3,sum/3,2)
    Base cases S(0,0,0,n)=1 i.e. integers found for all subsets matching the sum
    any -'ve input to S means, integer not found
    
'''
def part3(a,b,c,i):
    if (a,b,c)==(0,0,0):
        return 1
    if i>N or a<0 or b<0 or c<0:
        return 0
    k=part3(a-S[i-1],b,c,i+1)+part3(a,b-S[i-1],c,i+1)+part3(a,b,c-S[i-1],i+1)
    if k > 1:
        k=1
    return k
   
if __name__=='__main__':
    try:
        S=list(map(int,input("Enter integers:").split()))
    except:
        sys.exit('Enter only integers, seperated by spaces, e.g. 1 2 3')
    N=len(S)
    p=sum(S)/3
    k=part3(p,p,p,1)
    if k==1:
        print("partionable")
    else:
        print("Not partionable")
