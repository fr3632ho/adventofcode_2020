TREE = '#'
tot = col = 0
try:
    while True:
        line = input()
        if line[col%(len(line))] == TREE:
            tot += 1
        col += 3
except: EOFError
print(tot)
