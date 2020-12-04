import sys, re

def conds(c):
    return 1920 <= int(c['byr']) <= 2002 and len(c['byr']) == 4\
           and 2010 <= int(c['iyr']) <= 2020 and len(c['iyr']) == 4\
           and 2020 <= int(c['eyr']) <= 2030 and len(c['eyr']) == 4\
           and (('cm' in c['hgt'] and 150 <= int(c['hgt'].strip('cm')) <= 193) or ('in' in c['hgt'] and 59 <= int(c['hgt'].strip('in')) <= 76))\
           and all(char in "#abcdef0123456789" for char in c['hcl']) and len(c['hcl']) == 7\
           and c['ecl'] in {'amb','blu','brn','gry','grn','hzl','oth'}\
           and len(c['pid']) == 9 and c['pid'].isdigit()

keys = {'byr', 'iyr', 'eyr', 'hgt','hcl','ecl','pid'}
passports = sys.stdin.read().strip().split('\n\n')
tot = 0
for p in passports:
    p = re.split('\s', p)
    c = dict(i.split(':') for i in p)
    if all(key in c for key in keys):
         if conds(c):
            tot += 1
print(tot)
