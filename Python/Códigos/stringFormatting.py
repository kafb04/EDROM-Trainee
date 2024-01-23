def print_formatted(number):
    tam = len(bin(n)[2:])
    for i in range(1, n+1):
        decimal = str(i).rjust(tam)
        octal = oct(i)[2:].rjust(tam)
        hexadecimal = hex(i)[2:].upper().rjust(tam)
        binario = bin(i)[2:].rjust(tam)
        print(f"{decimal} {octal} {hexadecimal} {binario}")
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)