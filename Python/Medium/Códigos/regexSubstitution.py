import re

n = int(input())

for i in range(n):
    a = input()
    a = re.sub(r"(?<=\s)(&&)(?=\s)", r"and", a)
    a = re.sub(r"(?<=\s)(\|\|)(?=\s)", r"or", a)
    print(a)