xmas = []
with open('./day_9/source.txt') as source:
    for line in source:
        line = line.strip()
        xmas.append(int(line))
twfive = []


def isvalid(num, twfive):
    for item in twfive:
        for s in twfive:
            if s != item:
                if num == s+item:
                    return True
            else:
                continue
    return False


for i, item in enumerate(xmas):
    if i < 25:
        twfive.append(item)
        continue
    if isvalid(item, twfive):
        twfive.pop(0)
        twfive.append(item)
        continue
    else:
        print(f"{item} invalid.")
        invalidnum = item
        break
# part 2
summed = []
isvalid = False
for i, item in enumerate(xmas):
    if isvalid == True:
        break
    summed.append(item)
    for s in xmas[i+1:]:
        summed.append(s)
        if sum(summed) == invalidnum:
            print(f"encryption weakness: {min(summed)+max(summed)}")
            isvalid = True
            break
        elif sum(summed) > invalidnum:
            summed.clear()
            break
