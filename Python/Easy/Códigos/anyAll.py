N = int(input())
lista = list(map(int, input().split()))
print(all(num > 0 for num in lista) and any(str(num) == str(num)[::-1] for num in lista))