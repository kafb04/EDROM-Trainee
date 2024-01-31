import re
for _ in range(int(input())):
    if re.search(r'^[789]\d{9}$', input()):
        print("YES")
    else:
        print("NO")