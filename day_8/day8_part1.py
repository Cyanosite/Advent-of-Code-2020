acc = 0
ran = []
instruction = []
inst_num = []
with open('./day_8/source.txt', 'r') as source:
    for line in source:
        line = line.strip().split()
        instruction.append(line[0])
        inst_num.append(line[1])
i = 0
ran.append(len(instruction))
while(i not in ran):
    if instruction[i] == 'nop':
        i += 1
        continue
    elif instruction[i] == 'acc':
        ran.append(i)
        acc += int(inst_num[i])
        i += 1
        continue
    elif instruction[i] == 'jmp':
        i += int(inst_num[i])
        continue
print(f"The value of the accumulator: {acc}")
