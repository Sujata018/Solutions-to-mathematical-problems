# Count total number of squares in a square grid of n x n squares
#
# Provide dimension in variable n below.
#

n = 4
count = 0

for i in range (1,n+1):
    count += pow((n - i+1),2)
    
print (count)
