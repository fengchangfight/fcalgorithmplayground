from utils import randIntegerArrayGenerator
#############THE QUESTION IS###########
# given N integers, N is even, and a single integer k, pair N integers inside so that for each pair, <v1, v2>, v1+v2 can be exactly divided by k
# output form: list of integer pairs, list length of course should be N/2
#######################################gs


# intuition 1: it seems, we have to use dynamic programing to solve this issue, because each pair we form affects how other pairs are formed
# but if we do that, obviously this is becoming a O(n2) problem
# intuition 2: sum of array has to be divided by k if we can form the pairs, but the reverse might not be true
# intuition 3: consider obove 2 dynamic programming might not be a good idea here
# intuition 4: if the only seeminng possible way is not good, it might be a great idea to turn the problem itself into another equivalent form
# intuition 5: there is a similar question, about whether we can form pairs to make the sum of each and every pair a given constant
# if we can turn our problem into that form, then problem is solved
# intuition 6: use math!!! if a+b can be divided by k, it could be that both a and b can be divided by k, or, the remainder of a plus the remainder
# of b equals k(Can you prove it?), using this math, it's easy to to the problem turning, we turn the original array into an remainder array

class Pair(object):
    def __init__(self, v1, v2):
        self.val1 = v1;
        self.val2 = v2

    def sumDividedByK(self, k):
        if((self.val1+self.val2)%k==0):
            return True
        return False



# input_array should be array of integers, k is an integer to,
# output: True of False, depend on whether the pair can be found
def pairArray(input_array, k):
    print("divided by "+str(k))
    remainder = [m%k for m in input_array]
    # now the problem turns into find pairs in remainder array that sum up to k
    while(len(remainder)>0):
        val = remainder[0]
        remainder.remove(remainder[0])
        if(val!=0):
            if ((k - val) not in remainder):
                return False
            remainder.remove(k - val)
        else:
            if(0 not in remainder):
                return False
            remainder.remove(0)
    return True


# sample input:
for i in range(100):
    input = randIntegerArrayGenerator(10, 1, 30)
    print(input)
    print(pairArray(input, 5))
    print("========================")

