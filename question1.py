from utils import randIntegerArrayGenerator
# input：an array of integer, let's call it A:
# constraint： A[i]<A[j], i<j
# optimization goal： maximize(j-1)

# intuition 1: if not using any existing knowledge of the array, we have to compare each 2 elements of the array,
# which is obviously O(n2).

# intuition 2: let's fix the right side index, if there exist an left side index i, satisisfy the constraint, than any element that is small than
# A[i] on the left side of i would be a greater choice, which means, for any incremented list, only the leftmost element could be the candidate for
# the one for choice, the others in the list are just not possible.  e.g. there is a sub list [3,4,5], sublist don't have to be consecutive,
# but needs to maintain the order it occurs in the original list, only 3 could be the left-side candidate,
# 4 and 5 are just not possible, so this is a very useful way to exclude useful element! but how do we use this feature? that is a higher level
# question.

# intuition 3: thinking in a symmetry way, if there is an incrementing sub list, only the right-most candidate could be the candidate,
# e.g. there is a sub list [3,4,5], only 5 could be the candidate, don't even need to think about 3 and 4, because, if any of the 2 is a choice,
# 5 would be a better choice

# intuition 4: can we pick out the subset of the possible left-end candidates and right-end candidates? and then do something?

# intuition 5: how many such increment list do we need to pick? every increasing interval? or just one is enough?

# intuition 6: think in a subsequence way when dealing with array(not substring)

# intuition 7 think about fixing the left side(one side), and move from the other side，
# no move back and forth, think about why this is correct and prove it

# intuition 8, when we want to exclude a choice, we can prove it's correct by providing aother obviously better choice

# intuition 9, think about equal case, which is very very very important

input = randIntegerArrayGenerator(10, 1,30)

def findDecreasingSubSequenceIndex(input_array):
    result = []
    for i in range(len(input_array)):
        if(len(result)<1):
            result.append(i)
        elif(input_array[i]<input_array[result[-1]]):
            result.append(i)
    return result


#sample input
#input = [26, 3, 24, 16, 10, 14, 22, 1, 19, 1]
print(input)


decIndex = findDecreasingSubSequenceIndex(input)
print(decIndex)
j = len(input)-1
iIndex = len(decIndex)-1
i = decIndex[iIndex]

maxDistance = j-i

while(True):
    iIndex-=1
    if(iIndex<0):
        break
    i = decIndex[iIndex]
    if(input[i]<=input[j]):
        newDistance = j-i
        if(newDistance>maxDistance):
            maxDistance = newDistance
        continue
    else:
        while(input[i]>input[j]):
            j-=1
        newDistance = j-i
        if(newDistance>maxDistance):
            maxDistance = newDistance

print(maxDistance)


