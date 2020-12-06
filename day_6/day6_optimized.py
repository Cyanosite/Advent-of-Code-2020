answers, common_answers = [], []


def getAnswers(answer):
    return len(set(answer))


def getCommonAnswers(answer):
    return len(set(answer[0]).intersection(*answer))


for i in open('source.txt').read().split('\n\n'):
    answers.append(getAnswers(i.replace('\n', '')))
    common_answers.append(getCommonAnswers(i.strip().split('\n')))

print(sum(answers))
print(sum(common_answers))
