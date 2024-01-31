import re
n = int(input())
for i in range(0, n):
    try:
        re.compile(input())
        print(True)
    except Exception:
        print(False)
