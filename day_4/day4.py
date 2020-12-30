passport = open('./day_4/source.txt').read().split('\n\n')
passports = []
for item in passport:
    passports.append(item.split())


def program(passports):
    atof = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2',
            '3', '4', '5', '6', '7', '8', '9']
    eyecolors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid_passports = 0
    valid_secure = 0
    for s in passports:
        temp = 0
        tempsecure = 0
        for item in s:
            key, value = item.split(":")
            if key == 'byr':
                temp += 1
                if 1920 <= int(value) <= 2002:
                    tempsecure += 1
            if key == 'iyr':
                temp += 1
                if 2010 <= int(value) <= 2020:
                    tempsecure += 1
            if key == 'eyr':
                temp += 1
                if 2020 <= int(value) <= 2030:
                    tempsecure += 1
            if key == 'hgt':
                temp += 1
                height, unit = value[:-2], value[-2:]
                if unit == 'cm':
                    if 150 <= int(height) <= 193:
                        tempsecure += 1
                elif unit == 'in':
                    if 59 <= int(height) <= 76:
                        tempsecure += 1
            if key == 'hcl':
                temp += 1
                templetter = 0
                if value[0] == '#':
                    for letter in value[1:]:
                        if letter in atof:
                            templetter += 1
                    if templetter == 6:
                        tempsecure += 1
            if key == 'ecl':
                temp += 1
                if value in eyecolors:
                    tempsecure += 1
            if key == 'pid':
                temp += 1
                if len(value) == 9:
                    tempsecure += 1
        if temp == 7:
            valid_passports += 1
        if tempsecure == 7:
            valid_secure += 1
    return f"Part1: {valid_passports}\nPart2: {valid_secure}"


print(program(passports))
