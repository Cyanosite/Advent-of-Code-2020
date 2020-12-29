instruction = []
inst_num = []
with open('source.txt', 'r') as source:
    for line in source:
        line=line.strip().split()
        instruction.append(line[0])
        inst_num.append(line[1])
def run(instructs, inst_nums, num):
    acc=0
    i=0
    ran=[len(instructs)]
    if instructs[num]=='nop':
        instructs[num]='jmp'
    elif instructs[num]=='jmp':
        instructs[num]='nop'
    while(i not in ran):
        if instructs[i] == 'nop':
            i+=1
            continue
        elif instructs[i] == 'acc':
            ran.append(i)
            acc+=int(inst_nums[i])
            i+=1
            continue
        elif instructs[i] == 'jmp':
            i+=int(inst_nums[i])
            continue
    if len(instructs)<=i:
        print(acc)
        return True
    else:
        return False
terminates = False
s=0
while (terminates==False):
    terminates = run(instruction, inst_num, s)
    s+=1