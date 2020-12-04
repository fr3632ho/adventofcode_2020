cid = 'cid'
tot = 0
try:
    row = 0
    while True:
        lines = [i.split(':')[0] for i in input().split()]
        while True:
            try:
                q = input().split()
            except EOFError:
                break
            if len(q) == 0: break
            lines += [i.split(':')[0]  for i in q]

        lines = set(lines)
        if len(lines) >= 7 and cid not in lines:
            tot += 1
        elif len(lines) == 8:
            tot += 1
except: EOFError
print(tot)
