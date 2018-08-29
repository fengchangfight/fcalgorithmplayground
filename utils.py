from random import randint

# both start and int are inclusive 记住！！！
def randIntGenerator(start, end):
    return randint(start, end)


# generate <size> integer within range start and end(both inclusive)
def randIntegerArrayGenerator(size, start, end):
    result = []
    for i in range(size):
        result.append(randIntGenerator(start, end))
    return result

# this should use the first element as the pivot, move all element smaller to its left, and return its final position index
def partition(input_array, start_index, end_index, reverse=False):
    pivot = input_array[start_index]
    pivot_index = start_index
    for i in range(start_index+1, end_index+1):
        if((reverse==False and input_array[i]<pivot) or (reverse and input_array[i]>pivot)):
            tmp=input_array[pivot_index+1]
            input_array[pivot_index+1]=input_array[i]
            input_array[i]=tmp

            tmp = input_array[pivot_index]
            input_array[pivot_index] = input_array[pivot_index + 1]
            input_array[pivot_index+1] = tmp

            pivot_index+=1
    return pivot_index