N, X = list(map(int, input().split()))
marks = []
for i in range(X):
    marks.append(list(map(float, input().split())))
    
marksList = list(zip(*marks))

for i in range(len(marksList)):
    print(sum(marksList[i])/X)