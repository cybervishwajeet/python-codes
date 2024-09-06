import itertools

'''numbers = [1, 2, 3]
combinations = list(itertools.combinations(numbers, 2))
'''
def combinations(lst, r):
    result = []
    if r == 0:
        return [[]]
    for i in range(len(lst)):
        rest = lst[i+1:]
        for c in combinations(rest, r-1):
            result.append([lst[i]] + c)
    return result

numbers = [1, 2, 3]
combinations = combinations(numbers, 2)

print(combinations)
