import sys

def part2(s):
    global data
    window = [0, 1]
    while window[1] < len(data):
        slice = data[window[0]:window[1]]
        curr_sum = sum(slice)
        if curr_sum == s:
            return min(slice) + max(slice)
        if curr_sum < s:
            window[1] += 1
        if curr_sum > s:
            window[0] += 1
        if window[1] == window[0]:
            window[1] += 1

def part1(K):
    global data
    indx = K
    window = [0, K]
    while indx <= len(data):
        if not any(i+j==data[indx] for i in data[window[0]:window[1]] for j in data[window[0]:window[1]]):
            return data[indx]
        #map(lambda x : x + 1, window)
        window[0] += 1
        window[1] += 1
        indx += 1
    return data[indx]


data = list(map(int, sys.stdin.read().strip().split('\n')))

p1 = part1(25)
print(part2(p1), p1)
