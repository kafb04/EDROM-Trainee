import re

N = int(input())

for i in range(N):
    css = input()
    matches = re.findall('(?<!^)(#(?:[\da-f]{3}){1,2})', css,flags=re.I)
    if matches:
        print(*matches, sep="\n")