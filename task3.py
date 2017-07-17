a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for q in range(len(b) + 1):
    if a.count(q) in (a and b):
        c.append(q)
print(c)
