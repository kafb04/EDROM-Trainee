x, k = map(int, input().split())
p = input()
var = {'x': x}
res = eval(p, var)
print(res == k)