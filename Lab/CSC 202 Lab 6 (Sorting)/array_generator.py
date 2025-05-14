import random

def random_array(size):
    output = []
    for i in range(size):
        output.append(random.randint(0,size ** 2))
    return output

def ordered_array(size):
    output = []
    for i in range(size):
        output.append(i ** 3)
    return output