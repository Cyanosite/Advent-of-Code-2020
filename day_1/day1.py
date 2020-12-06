numbers = []
for i in open('source.txt'):
    numbers.append(int(i.strip()))
for i in numbers:
    for s in numbers:
        if i + s == 2020:
            print(i * s)
        for n in numbers:
            if i + s + n == 2020:
                print(i * s * n)
