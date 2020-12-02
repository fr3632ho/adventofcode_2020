
tot = 0
try:
    while True:
        query = input().split()
        low, high = map(lambda x: int(x) - 1, query[0].split('-'))
        tot += (query[-1][low]==query[1][0])^(query[-1][high]==query[1][0])
except: EOFError

print(tot)
