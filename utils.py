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


print(randIntegerArrayGenerator(10, 1,30))