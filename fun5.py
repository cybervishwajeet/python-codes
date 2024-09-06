def count_lower_upper(stri):
    d = {"Uppercase": 0, "lowercase": 0}
    for c in stri:
        if c.isupper():
            d["Uppercase"] += 1
        elif c.islower():
            d["lowercase"] += 1
    print("original string:", stri)
    print("no. of Upper case:", d["Uppercase"])
    print("no. of Lower case:", d["lowercase"])
str1 = "Vedant Kale"
count_lower_upper(str1)
