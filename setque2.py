#what will be the output for the following
a={1,2,3,4,5,6,7}
b={1,2,3,4,5,6,7}
c={1,2,3,4,5,6,7}
d={1,2,3,4,5,6,7}
e={3,4,1,0,2,5,8,9}
a |= e
print(a)
b &= e
print(b)
c -= e
print(c)
d ^= e
print(d)
