import sys
data = sys.stdin.read().strip().split('\n\n')
p1 = p2 = 0
for group in data:
    p1 += len(set("".join(group.split('\n')))) # part 1
    l = group.split('\n')
    n, d = len(l), dict()
    for letter in "".join(l):
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
        p2 += d[letter] == n

print(p1, p2)
