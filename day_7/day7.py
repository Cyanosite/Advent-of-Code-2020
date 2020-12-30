import time
start_time = time.time()
bags = {}

with open('./day_7/source.txt', 'r') as source:
    for line in source:
        line = line.strip().split()
        bags[f"{line[0]} {line[1]}"] = []
        for i, item in enumerate(line):
            if i <= 3:
                continue
            if i % 4 == 0:
                bags[f"{line[0]} {line[1]}"].append(
                    {f"{line[i + 1]} {line[i + 2]}": item})
#  PART 1


def contain(bag):
    shiny = False
    if bag in bags.keys():
        for items in bags[bag]:
            for key in items.keys():
                if key == 'shiny gold':
                    return 1
                elif key == 'other bags.':
                    return 0
                else:
                    if contain(key) == 1:
                        shiny = True
    return 1 if shiny else 0


containcount = 0
for item in bags.keys():
    containcount += contain(item)

print(containcount)
print(f"{time.time() - start_time} seconds")