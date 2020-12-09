import sys

def part2(xs, s):
    f = False
    for i in range(len(xs)-1, -1, -1):
        l = [xs[i]]
        curr_sum = s-xs[i]
        for j in range(i-1, -1, -1):
            if j < 0 or curr_sum < 0:
                break
            curr_sum -= xs[j]
            l.append(xs[j])
            if curr_sum == 0:
                f = True
                break
        if f:
            break

    l.sort()
    return l[0] + l[-1]


K = 25
data = list(map(int, sys.stdin.read().strip().split('\n')))
indx = 25
ans = -1
found = False
while indx <= len(data):
    for i in range(indx-K,indx):
        for j in range(indx-K, indx):
            a, b = data[i], data[j]
            if a==b:
                continue
            q = data[indx]
            if a + b == q:
                found = True
                break
        if found:
            break
    if not found:
        break
    found = False
    indx += 1

p1 = data[indx]
print(p1, part2(data[:indx], p1))
