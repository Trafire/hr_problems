from collections import Counter


def get_data():
    n = int(input())
    return [input() for i in range(n)]


def output(answer: Counter):
    print(len(answer))
    print(' '.join([str(answer.get(a)) for a in answer]))


data = get_data()
counter = Counter(data)
output(counter)
