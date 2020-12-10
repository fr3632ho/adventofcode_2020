from heapq import heappush, heappop
from collections import defaultdict
import sys

def count(ys, start, goal):
    global dp
    k = (len(ys), start)

    if k in dp:
        return dp[k]
    ways = 0
    if goal - start <= 3:
        ways += 1
    if not ys:
        return ways
    if ys[0] - start <= 3:
        ways += count(ys[1:], ys[0], goal)

    ways += count(ys[1:], start, goal)
    dp[k] = ways
    return ways

def vectorized_memo():
    global xs
    xs.insert(0, 0)
    memo = [0]*len(xs)
    memo[0] = 1
    for i in range(len(xs)):
        for j in range(i+1, len(xs)):
            if xs[j] - xs[i]  > 3: break
            memo[j] += memo[i]

    print(memo[len(xs)-1])

def part2():
    global m, xs
    mem = defaultdict(int)
    mem[0] = 1
    for block in xs:
        mem[block] = mem[block-1] + mem[block - 2] + mem[block - 3]

    return max(mem.values())

def part1():
    global l
    ans = [0]*3
    ans[2] += 1
    curr = 0
    while l:
        lo, hi = heappop(l)
        if curr >= lo:
            ans[hi-curr-1] += 1
            curr = hi
            continue
        break

    return ans[0]*ans[2]

l = []
xs = []
m = -1
for line in sys.stdin:
    q = int(line)
    xs.append(q)
    bound = (0 + (q-3 > 0)*(q-3), q)
    heappush(l, bound)


xs.sort()
xs.append(xs[-1] + 3)
dp = dict()
print(vectorized_memo())
