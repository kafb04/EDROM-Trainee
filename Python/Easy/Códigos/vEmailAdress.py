import re

x = int(input())

for i in range(x):
    nome, email = input().split()
    
    pattern = re.compile(r'^[A-Z0-9]([A-Z0-9_.-]+)@([A-Z]+)\.([A-Z]{1,3})$', re.I)
    if re.match(pattern, email[1:-1]) is not None:
        print(nome, email)