import sys


class Stack:
    def __init__(self, name):
        self.values = list(name)

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def top(self):
        return self.values[-1]

    def __len__(self):
        return len(self.values)

    def __str__(self):
        result = ''
        for x in self.values:
            result += str(x) + ' '
        return result

exec(open('input.txt'))
