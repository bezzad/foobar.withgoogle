
# 15: 1111
# +1=16
# /2=8
# /2=4
# /2=2
# /2=1

# 13:     1101
# -1=12   1100
# /2=6     110
# /2=3      11  
# -1=2      10    ==> ... and len(lstBinary) > 2
# /2=1       1


#      2^9 2^8     2^6   2^4  2 1 0
#      512 256 128 64 32 16 8 4 2 1
# 855:  1   1   0   1  0  1 0 1 1 1
# 1  +1=856    ‭  ۱۱۰۱۰۱۱۰۰۰‬  +1 = Reduce 1 in Binary
# 2  /2=428 ‭      ۱۱۰۱۰۱۱۰۰‬  Shift to Right = /2
# 3  /2=214 ‭       ۱۱۰۱۰۱۱۰‬  Shift to Right = /2
# 4  /2=107        ‭ ۱۱۰۱۰۱۱‬  Shift to Right = /2
# 5  +1=108         ۱۱۰۱۱۰۰‬  +1 = Reduce 1 in Binary
# 6  /2=54           ۱۱۰۱۱۰‬  Shift to Right = /2
# 7  /2=27            ۱۱۰۱۱‬  Shift to Right = /2
# 8  +1=28            ۱۱۱۰۰‬  +1 = Reduce 1 in Binary
# 9  /2=14 ‭            ۱۱۱۰‬  Shift to Right = /2
# 10 /2=7            ‭   ۱۱۱‬  Shift to Right = /2
# 11 +1=8              ‭۱۰۰۰‬  +1 = Reduce 1 in Binary
# 12 /2=4              ‭ ۱۰۰‬  Shift to Right = /2
# 13 /2=2              ‭  ۱۰‬  Shift to Right = /2
# 14 /2=1              ‭   ۱‬  Shift to Right = /2


def addSub(lstBin, isAdd=True):
    completed = False
    for i in range(len(lstBin) - 1, -1, -1):
        if(lstBin[i] == "1"): # on 1
            lstBin[i] = '0'
            if(not isAdd):
                completed = True
                break
        else: # on 0
            lstBin[i] = '1'
            if(isAdd):
                completed = True
                break

    if(not completed): # actully happened in Add operation
        lstBin.insert(0, "1")

    return lstBin


def answer(n):
    counter = 0
    num = int(n, 10)
    print("Input", num)

    print("")

    binNum = "{0:b}".format(int(n, 10))
    print("Input Binary", binNum)

    lstBinary = list(binNum)

    while(len(lstBinary) > 1 or lstBinary[0] != "1"):
        if(int(lstBinary[len(lstBinary)-1]) % 2 == 0):  # even
            lstBinary.pop() # bin shift right = dec/2
        else:  # odd
            if(lstBinary[len(lstBinary)-2] == "1" and len(lstBinary) > 2):  # N...N11 ==> +1 to reduce count of 1 (odd numbering) in string
                addSub(lstBinary, True)
            else:  # N...N01 ==> -1 to reduce count of 1 (odd numbering) in string
                addSub(lstBinary, False)

        print("after", lstBinary.count("1"), lstBinary)

        counter += 1

    return counter


# --------------------------- TEST -------------------------------------------

import random
# generate test input
rendomNumber = "2"
for x in range(400):
    rendomNumber += str(random.randint(0, 9))
print("answer", answer(rendomNumber))
