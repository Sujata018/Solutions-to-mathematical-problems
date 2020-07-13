# In how many ways six dancers, A,B,C,D,E,F can perform in a solo competition if A performs after B #

from itertools import permutations

perm = permutations([1,2,3,4,5,6])
count = 0
countBA = 0
for i in list(perm):
    if i.index(1) > i.index(2):
        countBA += 1
    count += 1
print ("Six dancers can dance in ", count, " ways")
print ("A can dance after B in ", countBA, " ways")
