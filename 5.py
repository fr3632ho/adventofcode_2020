import sys

data = sys.stdin.read().strip().split('\n')

# [0, 127] rows, 7 characters => log2(128) = 7
m = 0
seat_ids = []
for card in data:
    l, h  = 0, 127 # l will be row
    _l, _h = 0, 7
    rows, cols = card[:7], card[7:]
    i = 0
    while l <= h:
        if i < 3:
            c = _l + (_h - _l)// 2
            if cols[i] == 'R':
                _l = c + 1
            else:
                _h = c - 1
        mid = l + (h - l)// 2
        if rows[i] == 'F':
            h = mid - 1
        else:
            l = mid + 1
        i+=1

    seat_ids.append(l*8 + _l)
    m = max(m, l*8 + _l)

seat_ids.sort()
prev = seat_ids[0]
id = -1
for i in range(1, len(seat_ids)):
    if seat_ids[i] - prev == 2:
        id = seat_ids[i] - 1
        break
    prev = seat_ids[i]
print(m, id)
