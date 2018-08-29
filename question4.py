from utils import randIntegerArrayGenerator
from utils import partition
#############THE QUESTION IS###########
# given an array of integer and an integer k,  find the one sub set of the array that sums bigger than k, and has the least number of elements
# e.g. given [5,4,3,2,1] and 11, the sub list should be [5,4,3] because 5+4+3>11 and you can't find any other subset that satisfiy this constraint with fewer elements
#######################################

#input = [1,3,5,2,4]
input = randIntegerArrayGenerator(10, 1, 30)
k=11

def sum(input_array, start_index, end_index):
    s = 0
    for i in range(start_index, end_index+1):
        s+=input_array[i]
    return s

def subArray(input, k, start, end):
    if(start>end):
        return []
    if(start==end):
        if(input[start]>k):
            return [input[start]]
        else:
            return []

    index = partition(input, start, end, True)
    s = sum(input, start, index)
    if (s <= k):
        return input[start:index+1]+subArray(input, k-s, index+1, end)
    else:
        return subArray(input, k, start, index)

print(input)
re = subArray(input, 50, 0, len(input)-1)

print(re)



