#code by Vedant Kale H3
def tuplelist():
    result = [(x, x*2, x*3) for x in range(1, 11)]
    return result
tuples_list = tuplelist()
for item in tuples_list:
    print(item)