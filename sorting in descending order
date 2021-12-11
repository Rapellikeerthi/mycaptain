def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d

print (most_frequent('mississippi'))
a1 = {'m':1, 'i':4, 's':4, 'p':2}
a1_sorted_keys = sorted(a1, key=a1.get, reverse=True)
for r in a1_sorted_keys:
    print(r, a1[r])
