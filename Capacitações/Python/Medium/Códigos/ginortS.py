s = input()

string = sorted(s, key=lambda x: (x.isdigit(), x.isdigit() and int(x) % 2 == 0, x.isupper(), x))

result = ''.join(string)

print(result)
