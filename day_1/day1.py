numbers = [int(i) for i in open('./day_1/source.txt').read().strip().split()]
part1 = set()
part2 = set()
for i in numbers:
    for s in numbers:
        if i + s == 2020:
            part1.add(i * s)
        for n in numbers:
            if i + s + n == 2020:
                part2.add(i * s * n)
print(f'Part1: {part1}')
print(f'Part2: {part2}')