def answer(num_buns, num_required):
    x = [[0 for x in xrange(5)] for y in xrange(6)] 
    x[0].append(123)
    print("x", x)

    c = num_buns - num_required + 1  # count of each number
    u = num_required  # count of used unique numbers
    # (u * c) % num_buns == 0 
    if(c*num_required > num_buns):
        u = num_buns

    print("c", c, "u", u)
    result = []
    # if (num_buns < num_required):
    #     # no group of (num_required - 1) bunnies can
    #     return result

    # countOfFilled = 0
    # usedNumbersCounter = []
    # for bun in xrange(num_buns):
    #     for req in xrange(num_required):
    #         result[bun]
    #         # result.append(
    #         # usedNumbersCounter[req] += 1

    return result

# c = count of each number = num_buns - num_required + 1
# u = count of used unique numbers = num_required + x_nums
# (u * c) % num_buns == 0      ---->     ((num_required + x_nums)*c) % num_buns == 0
# if(c*num_required > num_buns) u = num_buns
# else u = num_required
# answer(6, 3): c=4
# [0,1,2,4]
# [0,1,3,4]
# [0,1,4,5]
# [0,2,3,5]
# [1,2,3,5]
# [2,3,4,5]


print(answer(3, 1))
print("----------------------")
print(answer(2, 2))
print("----------------------")
print(answer(2, 1))
print("----------------------")
print(answer(9, 1))
print("----------------------")
print(answer(3, 2))
print("----------------------")
print(answer(4, 5))
print("----------------------")
print(answer(4, 4))
print("----------------------")
print(answer(4, 3))
print("----------------------")
print(answer(5, 3))
print("----------------------")
print(answer(6, 3))
print("----------------------")
