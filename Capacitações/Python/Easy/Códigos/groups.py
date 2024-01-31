li = list(input())

result = -1
for i in range(len(li)-1):
    char = li[i] 
    if char.isalnum() and char == li[i+1]:
        result = char
        break
print(result)