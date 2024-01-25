T = int(input())

for i in range(T):
    string = input()
    try:
        float_value = float(string)
        if '.' in string or 'e' in string.lower():
            print(True)
        else:
            print(False)
    except ValueError:
        print(False)
