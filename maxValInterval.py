import sys      # for system exit in case of invalid input 

table=[]	# global variable to store the best intervals list

'''
Function for merging sorted lists. Used in merge sort.
'''
def merge(interval,low,mid,high):           # merge sorted intervals low to mid, and mid+1 to high 
    i=low                                   # starting indices of intervals
    j=mid+1
    k=0                                     # index for merged interval
    B=[[] for _ in range(high-low+1)]       # initialise list to keep merged intervals
    while (i<=mid and j<=high):             # loop while elements left in both lists
        if interval[i][1]<= interval[j][1]: # among next elements from two lists, copy the one having lower finish time, to the merged list 
            B[k]=interval[i]
            i += 1
        else:
            B[k]=interval[j]
            j += 1
        k += 1
    if i<= mid:                             # copy residual elements left in either of the two lists
        B[k:k+mid+1-i]=interval[i:mid+1]
        k += mid-i+1
    if j<= high:
        B[k:]=interval[j:high+1]
    interval[low:high+1]=B
    
    return interval                         # return merged sorted list

'''
Merge sort 
'''
def mergeSort(interval,low,high):

    if low>=high:                           # base condition, only one element for sorting
        return interval
    
    mid=(low+high)//2                      
    interval=mergeSort(interval,low,mid)    # sort lower half
    interval=mergeSort(interval,mid+1,high) # sort upper half
    
    merge(interval,low,mid,high)            # merge lower and upper halves into a sorted list
   
    return interval

'''
Do binary search in the table of intervals to find the interval having maximum finish time which is lower than 
the start time of the search interval.
The intervals are sorted in ascending order of finish time.
'''
def binarySearch(s,low,high):               # do binary search with key as s, in range low to high in table
    
    if table[low][1]>s:                     # no overlapping intervals
        return low-1
    if low >=high:                          # interval found
        return low
    
    mid=(low+high)//2
    if table[mid][1]==s:                    # interval found
        return mid
    elif table[mid][1]<s:                   # search in upper half
        return binarySearch(s,mid+1,high)
    else:                                   # search in lower half
        return binarySearch(s,low,mid-1)           

'''
Function to add a single interval to the table, if no other existing intervals already have higher value than it.
'''
def addSingleInterval(interval):

    global table

    if len(table)==0 or interval[2] > table[-1][2]: # if no intervals are there in table, or current interval value is more than last interval in the tab;e, then add
        interval.append(str(interval))
        table.append(interval)

'''
Function to merge an interval to an existing interval in the table.

'''
def mergeInterval(interval):

    global table

    maxFinishIndex=binarySearch(interval[0],0,len(table)-1) # find the interval with maximum finish time that is lower than the start time of the interval to be merged with
    if maxFinishIndex >=0 and (table[maxFinishIndex][2]+interval[2])>table[-1][2]: # if sum of their values are > maximum value interval in table, then add
        t=table[maxFinishIndex]
        newVal=t[2]+interval[2]
        table.append([t[0],interval[1],newVal,t[3]+','+str(interval)])

'''
This function returns the non-overlapping intervals having maximum total value, given a list of intervals and their values
'''
def maxValNonOverlap(intervals):
    
    global table
    
    for interval in intervals:                        # for each interval 
        if len(table)==0 or table[0][1]>interval[0]:  # if overlap with all existing intervals in the table
            addSingleInterval(interval)               # add individual interval
        else:                    
            mergeInterval(interval)                   # else merge with other intervals
    return table[-1][-1]                              # return (individual or merged) interval with maximum value 

'''
Main function.
Receives intervals from stdin.
Input: s1 f1 v1 s2 f2 v2 ... upto sn,fn,vn : n<- number of intervals entered. All integer values accepted.


'''
if __name__=='__main__':
    data=input("Enter start finish value triplets:").split()
    if len(data)%3 != 0:                             # exit, if discrepency in number of integers entered
        sys.exit("Invalid input. Enter <start1 finish1 value1 start2 finish2 value2 ... startn finishn valuen> ")
    try:                                             # create a list of intervals of the form (start time,finish time,value)
        intervals=[[int(data[i]),int(data[i+1]),int(data[i+2])] for i in range(0,len(data),3)]
    except:                                          # if non-numeric values intered, exit
        sys.exit("Enter numeric values only")
    
    mergeSort(intervals,0,len(intervals)-1)          # sort intervals in ascending order of finish time
    print("Non overlapping intervals with maximum value : ",maxValNonOverlap(intervals)) # get max non-overlapping subset