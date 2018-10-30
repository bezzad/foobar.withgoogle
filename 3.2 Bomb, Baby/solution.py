
import random


def getBigNumber(decNumber):
    decNumber
    for i in range(random.randint(10, 90)):
        decNumber = str(random.randint(0, 9)) + decNumber
    return decNumber

    # 7 4
    # 3 4
    # 3 1
    # 2 1
    # 1 1
    # 15 8
    # 7  8
    # 7  1
    # 6  1
    # 5  1
    # 4  1
    # 3  1
    # 2  1
    # 1  1


def answer(M, F):
    M = int(M, 10)
    F = int(F, 10)
    counter = 0

    print("{M:"+str(M) + ", F:"+str(F)+"}")

    while (M > 1 or F > 1):
        if (M % 2 == 0 and F % 2 == 0) or M < 1 or F < 1:
            return "impossible"
        if(M > F):
            counter += M/F
            M %= F
        else:
            counter += F/M
            F %= M

        if(M == 0 or F == 0): # is 1 step more than start point 1,1
            counter -= 1

        print("#" + str(counter) + ". {M:"+str(M) + ", F:"+str(F)+"}")

    return str(counter)


print("M:4, F:7", answer("4", "7"))
print("------------------------------")
print("M:2, F:7", answer("2", "7"))
print("------------------------------")
print("M:2, F:1", answer("2", "1"))
print("------------------------------")
print("M:14, F:7", answer("14", "7"))
print("------------------------------")
print("M:4, F:17", answer("4", "17"))
print("------------------------------")
print("M:41, F:7", answer("41", "7"))
print("------------------------------")
print("M:21, F:7", answer("21", "7"))
print("------------------------------")
print("M:22, F:7", answer("22", "7"))
print("------------------------------")
print("M:14, F:17", answer("14", "17"))
print("------------------------------")
print("M:50, F:7", answer("50", "7"))
print("------------------------------")
print("M:2, F:6456", answer("2", "6456"))
print("------------------------------")
print("M:BigNumber, F:7", answer(getBigNumber("1"), "7"))
print("------------------------------")
print("M:BigNumber, F:BigNumber", answer(getBigNumber("1"), getBigNumber("0")))
