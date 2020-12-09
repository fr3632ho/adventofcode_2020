import sys

def solve(ins):
    visited = set()
    indx = acc = 0
    while 0 <= indx < len(ins):
        i, val = ins[indx]
        if indx in visited:
            break
        visited.add(indx)
        if i == 'jmp': indx += int(val)
        elif i == 'acc':
            acc += int(val)
            indx += 1
        else: indx += 1
    if indx>=len(ins): return acc
    return -1


data = sys.stdin.read().strip().split('\n')
ins = [data[i].split() for i in range(len(data))]
jmps = []
for c, i in enumerate(ins):
    if i[0] == 'jmp':
        jmps.append(c)

for j in jmps:
    instruction, val = ins[j]
    ins[j] = ('nop', val)
    ans = solve(ins)
    if ans != -1:
        print(ans)
        break
    ins[j] = (instruction, val)
