from collections import defaultdict, deque
import sys, re

def part1():
    global data
    graph = defaultdict(list)
    for query in data:
        bags = re.split(' \d', query)
        if len(bags) <= 1:
            continue
        u = " ".join(bags[0].strip().split()[:2])
        for bag in bags[1:]:
            v = " ".join(bag.strip().split()[:2])
            graph[v].append(u)

    return bfs(graph)

def part2():
    global start, data
    graph = defaultdict(list)
    for q in data:
        q = q.split()
        u, q = " ".join(q[:2]), q[2:]
        for i in range(len(q)):
            if not q[i].isdigit():
                continue
            graph[u].append((" ".join(q[i+1:i+3]), int(q[i])))


    return dfsHelper(start, graph) - 1

def bfs(graph):
    global start
    count = -1
    visited = set()
    Q = deque([start])
    while Q:
        u = Q.popleft()

        if u in visited:
            continue

        visited.add(u)
        count += 1
        for n in graph[u]:
            if n not in visited:
                Q.append(n)
    return count

def dfsHelper(node, graph):
    global dp
    dp[node] = 1
    for n, weight in graph[node]:
        if n in dp:
            dp[node] += weight * dp[n]
        else:
            dp[node] += weight* dfsHelper(n, graph)

    return dp[node]

data = sys.stdin.read().strip().split('\n')
start, n, dp = "shiny gold", len(data), dict()

print(part1(),part2())










#
