answers, common_answers = [], []


def getAnswers(answer):
    return len(set(answer))


def getCommonAnswers(answer):
    return len(set(answer[0]).intersection(*answer))


for i in open('./day_6/source.txt').read().split('\n\n'):
    answers.append(getAnswers(i.replace('\n', '')))
    common_answers.append(getCommonAnswers(i.strip().split('\n')))

print(f'Part1: {sum(answers)}')
print(f'Part2: {sum(common_answers)}')
