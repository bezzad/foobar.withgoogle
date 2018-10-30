def answer(l):

    #  inputs: [1,6,7,9,12,36]
    #  outputs:
    #                              1 
    #                             /|\ 
    #          [1,9,36]          / | \ 
    #          [1,12,36]        /  |  \ 
    #          [6,12,36]       6---+   9 
    #          [1,6,12]         \ 12  / 
    #          [1,6,36]          \ | / 
    #                             \|/  
    #                             36
    # 
    # if (x divides y divides z):   
    # x ------> y -------> z 
    #    input     output
    # 
    # inputs[y] = x
    # outputs[y] = z

    inputs = {}   # count of inputs to a number
    outputs = {}  # count of outputs from a number
    counter = 0

    for i in xrange(len(l)):
        for j in xrange(i+1, len(l)):
            if(l[j] % l[i] == 0):  # l[i] divides l[j]
                inputs[j] = inputs.get(j, 0) + 1
                outputs[i] = outputs.get(i, 0) + 1
    for i in inputs:
        counter += inputs[i] * outputs.get(i, 0)

    return counter

# Test cases
# ==========

import random
def generateList(count):
    lst = []
    for i in xrange(1,count):
        lst.append(i*10 + random.randint(0,9))
    return lst

print("Inputs", [1, 2, 3, 6, 8])
print("Output", answer([1, 2, 3, 6, 8]))
print("-------------------------------")
print("Inputs", [1, 1, 1])
print("Output", answer([1, 1, 1]))
print("-------------------------------")
print("Inputs", [1, 2, 3, 4, 5, 6])
print("Output", answer([1, 2, 3, 4, 5, 6]))
print("-------------------------------")
print("Inputs", [3, 4, 5, 6, 8, 9])
print("Output", answer([3, 4, 5, 6, 8, 9]))
print("-------------------------------")
print("Inputs", [3, 9])
print("Output", answer([3, 9]))
print("-------------------------------")
print("Inputs", [1,6,7,9,12,36])
print("Output", answer([1,6,7,9,12,36]))
print("-------------------------------")
print("Inputs", [3,4,5,7,8,9,12,36,72])
print("Output", answer([3,4,5,7,8,9,12,36,72]))
print("-------------------------------")
print("Inputs", [3, 9, 12, 18, 24, 36, 48, 96])
print("Output", answer([3, 9, 12, 18, 24, 36, 48, 96]))
print("-------------------------------")
lst = generateList(10)
print("Inputs", lst)
print("Output", answer(lst))
print("-------------------------------")
lst = generateList(100)
print("Inputs", lst)
print("Output", answer(lst))
print("-------------------------------")
lst = generateList(1000)
print("Inputs", lst)
print("Output", answer(lst))
print("-------------------------------")
lst = generateList(2001)
print("Inputs", lst)
print("Output", answer(lst))
print("-------------------------------")


