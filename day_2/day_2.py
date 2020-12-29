occurrence = []
letter = []
password = []
valid = 0
validnew = 0
with open('./day_2/source.txt', 'r') as source:
    for item in source:
        parts = item.strip().split()
        occurrence.append(parts[0].split('-'))
        letter.append(parts[1][0])
        password.append(parts[2])

for i, item in enumerate(password):
    occurrencetemp = 0
    for s in item:
        if s == letter[i]:
            occurrencetemp += 1
    if int(occurrence[i][0]) <= occurrencetemp <= int(occurrence[i][1]):
        valid += 1
    if int(item[int(occurrence[i][0]) - 1] == letter[i]) != int(item[int(occurrence[i][1]) - 1] == letter[i]):
        validnew += 1
print(f'Part1: {valid}')
print(f'Part2: {validnew}')
