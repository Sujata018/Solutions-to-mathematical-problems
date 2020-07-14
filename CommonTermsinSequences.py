# Count number of common terms in two sequences
# S1 = {3,7,11,..., 407} = {3 + 4k}
# S2 = {2,9,16,..., 709} = {2 + 7m}
#
# Add start, step and end numerics for the two sequences below and run the program
#

start1 = 3
step1 = 4
end1 = 407

start2 = 2
end2 = 709
step2 = 7

count = 0
while start1 <= end1 and start2 <= end2:
    if start1 < start2 :
        start1 += step1
    elif start1 > start2 :
        start2 += step2
    else:
        count += 1
        start1 += step1
        start2 += step2
print (count)
