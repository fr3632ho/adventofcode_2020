xs = {'byr': (1920, 2002), # low, high
      'iyr':(2010, 2020), # low, high
      'eyr':(2020, 2030), # low, high
      'hgt':[(150, 193), (59, 76)], #cm vs inch, must contain unit in end
      'hcl':('#abcdef0123456789'), # Must contain hashtag (#) in beginning
      'ecl':{'amb','blu','brn','gry','grn','hzl','oth'}, #contaisn just one
      'pid': 9 # length of pid
      }

cid = 'cid'
tot = 0
try:
    while True:
        lines = [tuple(i.split(':')) for i in input().split()]
        while True:
            try:
                q = input().split()
            except EOFError:
                break
            if len(q) == 0: break
            lines += [tuple(i.split(':')) for i in q]

        lines = set(lines)
        if len(lines) < 7:
            continue

        ok = True # check for cid in lines
        if len(lines) == 7:
            for c, _ in lines:
                if c == cid:
                    ok = False;
                    break
        if not ok:
            continue

        check = True
        for k, v in lines:
            if k == cid:
                continue

            if k == 'byr' or k == 'iyr' or k == 'eyr':
                l, h = xs[k]
                check = l <= int(v) <= h
            elif k == 'hgt':
                if 'cm' in v:
                    l, h = xs[k][0]
                    check = (l <= int(v.strip('cm')) <= h)
                elif 'in' in v:
                    l, h = xs[k][1]
                    check = (l <= int(v.strip('in')) <= h)
            elif k == 'hcl':
                if len(v) != 7:
                    check = False
                    break

                s1 = xs[k]
                for s in v:
                    if s in s1: continue
                    check = False;
                    break

            elif k == 'ecl':
                check = v in xs[k]
            elif k == 'pid':
                check = len(v) == xs[k] and v.isdigit()

            if not check:
                break

        print(check, tot)
        tot += check

except: EOFError
print(tot)
