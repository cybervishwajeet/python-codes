#code by Vedant Kale H3
def create_list(l1,l2):
    l3=set(l1)&set(l2);
    return l3;
l1=[10,20,30,40,50]
l2=[30,40,50,60,70]

print("Intersection of two lists are:",create_list(l1,l2));