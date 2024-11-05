import operator
l = [(4, 1.93, '4x4 - 1.93 seconds\n'), (4, 2.29, '4x4 - 2.29 seconds\n'), (4, 2.42, '4x4 - 2.42 seconds\n'), (4, 2.44, '4x4 - 2.44 seconds\n'), (4, 2.48, '4x4 - 2.48 seconds\n'), (4, 2.57, '4x4 - 2.57 seconds\n'), (4, 2.74, '4x4 - 2.74 seconds\n'), (4, 2.8, '4x4 - 2.80 seconds\n'), (4, 2.85, '4x4 - 2.85 seconds\n'), (4, 2.92, '4x4 - 2.92 seconds\n'), (4, 2.92, '4x4 - 2.92 seconds\n'), (4, 2.93, '4x4 - 2.93 seconds\n'), (4, 2.95, '4x4 - 2.95 seconds\n'), (4, 3.2, '4x4 - 3.20 seconds\n'), (4, 3.7, '4x4 - 3.70 seconds\n'), (4, 3.78, '4x4 - 3.78 seconds\n'), (4, 34.01, '4x4 - 34.01 seconds\n'), (5, 2.32, '5x5 - 2.32 seconds\n'), (5, 2.65, '5x5 - 2.65 seconds\n'), (5, 2.68, '5x5 - 2.68 seconds\n'), (5, 3.19, '5x5 - 3.19 seconds\n'), (5, 3.34, '5x5 - 3.34 seconds\n'), (5, 3.45, '5x5 - 3.45 seconds\n'), (5, 3.5, '5x5 - 3.50 seconds\n'), (5, 3.67, '5x5 - 3.67 seconds\n'), (5, 3.7403340339660645, '5x5 - 3.74 seconds\n'), (5, 4.36, '5x5 - 4.36 seconds\n'), (5, 4.46, '5x5 - 4.46 seconds\n'), (5, 5.65, '5x5 - 5.65 seconds\n'), (5, 5.79, '5x5 - 5.79 seconds\n'), (5, 6.08, '5x5 - 6.08 seconds\n'), (5, 14.48, '5x5 - 14.48 seconds\n'), (5, 18.07, '5x5 - 18.07 seconds\n'), (7, 12.37, '7x7 - 12.37 seconds\n')]

s = sorted(l, key = operator.itemgetter(1))
s = sorted(s, key = operator.itemgetter(0), reverse= True)

for i in s:
    print(i[2], end="\r")

for i in s:
    assert i[0] <= i-1[0] 

print(l)