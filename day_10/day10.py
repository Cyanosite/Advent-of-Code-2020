adapters = sorted([int(i) for i in open('source.txt').read().split()])


def part1(adapters):
    jolt1 = 0
    jolt3 = 1
    for i, item in enumerate(adapters):
        if i == 0:
            if item == 1:
                jolt1 += 1
            elif item == 3:
                jolt3 += 1
            continue
        if item-adapters[i-1] == 1:
            jolt1 += 1
            continue
        elif item-adapters[i-1] == 3:
            jolt3 += 1
            continue
    return jolt1*jolt3


print(f"Part 1 answer: {part1(adapters)}")
