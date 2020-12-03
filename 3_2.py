from functools import reduce

col_slopes = [1, 3, 5, 7, 1]
TREE = '#'
totals = [0]*5
cols = [0]*5
row = 0
try:
    while True:
        line = input()
        for i in range(4):
            totals[i] += (line[cols[i]%len(line)] == TREE)
            cols[i] += col_slopes[i]
        if not row %2:
            totals[-1] += (line[cols[-1]%len(line)] == TREE)
            cols[-1] += col_slopes[-1]
        row += 1

except: EOFError
print(reduce(lambda x, y: x * y, totals))
