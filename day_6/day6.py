sumans = 0
sumeveryone = 0
source = []
group = []
with open('source.txt', 'r') as sourcetxt:
    for line in sourcetxt:
        source.append(line.strip())
for item in source:
    if item != '':
        group.append(item)
    elif item == '':
        answers = set()
        for value in group:
            for s in value:
                answers.add(s)
        sumans += len(answers)
        for k in answers:
            groupcount = 0
            for u in group:
                if k in u:
                    groupcount += 1
            if groupcount == len(group):
                sumeveryone += 1
        group = []
answers = set()
for value in group:
    for s in value:
        answers.add(s)
sumans += len(answers)
for k in answers:
    groupcount = 0
    for u in group:
        if k in u:
            groupcount += 1
    if groupcount == len(group):
        sumeveryone += 1
print(sumans)
print(sumeveryone)