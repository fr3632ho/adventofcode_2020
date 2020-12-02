tot = 0
try:
    while True:
        query = input().split()
        low, high = map(int, query[0].split('-'))
        tot += 1*(low<= query[-1].count(query[1][0]) <= high)
except: EOFError
print(tot)
