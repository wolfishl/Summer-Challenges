def two_sum(array, target):
    map = dict()
    solution = "no solution"
    for x in range(len(array)):
        if target - array[x] in map.keys():
            solution = [x, map[target - array[x]]]
        else:
            map[array[x]] = x
    return solution

