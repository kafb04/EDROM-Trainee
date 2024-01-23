def print_rangoli(size):
    str=''
    for i in range(size,0,-1):
        str+=chr(i+64).lower()
        if(len(str))==1:
            print(str.center(size*4-3,'-'))
        else:
            a='-'.join(str)
            b=a+a[len(a)-2::-1]
            desenho=b.center(size*4-3,'-')
            print(desenho)
    for i in range(size,1,-1):
        str=str[0:len(str)-1]
        if(len(str))==1:
            print(str.center(size*4-3,'-'))
        else:
            a='-'.join(str)
            b=a+a[len(a)-2::-1]
            desenho=b.center(size*4-3,'-')
            print(desenho)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)