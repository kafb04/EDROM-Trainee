def merge_the_tools(string, k):
    n = len(string)
    tam = n // k

    for i in range(tam):
        start = i * k
        end = start + k
        sub = string[start:end]

        arr = []
        for char in sub:
            if char not in arr:
                arr.append(char)

        print(''.join(arr))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)