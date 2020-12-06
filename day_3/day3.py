slopes = {(1, 1): 0, (3, 1): 0, (5, 1): 0, (7, 1): 0, (1, 2): 0}
for key, value in slopes.items():
    temp = 0
    for i, item in enumerate(open('source.txt', 'r')):
        if i % key[1] != 0:
            continue
        else:
            item = item.strip()
            if temp < len(item):
                if item[temp] == '#':
                    slopes[key] += 1
            else:
                temp = temp - len(item)
                if item[temp] == '#':
                    slopes[key] += 1
            temp += key[0]
results = []
final = 1
for value in slopes.values():
    results.append(value)
for i in range(len(results)):
    final *= results[i]
print(final)
