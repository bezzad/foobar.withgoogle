from itertools import combinations

def answer(num_buns, num_required):
    result = [[] for _ in xrange(num_buns)]

    if(num_buns < num_required):
        return result

    # repeat count of each unique number
    repeat = num_buns - num_required + 1

    # get all combinations of size repeat times bunnies
    groups = combinations(xrange(num_buns), repeat)

    # distribute numbers by generated groups to no group of (num_required - 1) bunnies can
    unique_num = 0
    for group in groups:
        for n in group:
            result[n].append(unique_num)
        unique_num += 1
        # print("by", group, "result", result)
    return result

if __name__ == "__main__":
    print("run in debugger...")
    print("=============================== TEST CASES ===============================")
    for i in xrange(1, 10):
        for j in xrange(0, 10):
            print("bunnies", i, "required", j)
            print(answer(i, j))
            print("------------------------------------------------------------------")
