# In how many ways six speakers, A,B,C,D,E,F can address a gathering if A speaks after B #

from itertools import permutations

perm = permutations([1,2,3,4,5,6])
count = 0
countBA = 0
for i in list(perm):
    if i.index(1) > i.index(2):
        countBA += 1
    count += 1
print ("Six speakers can address in ", count, " ways")
print ("A can speak after B in ", countBA, " ways")
