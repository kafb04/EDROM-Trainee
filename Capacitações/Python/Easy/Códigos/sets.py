def average(array):
    dif_num = set(array)
    soma_dif = sum(dif_num)
    qtd_dif = len(dif_num)
    result = soma_dif/qtd_dif
    return result

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)