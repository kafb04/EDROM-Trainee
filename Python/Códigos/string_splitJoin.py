def split_and_join(line):
    palavras = line.split(" ")
    result = "-".join(palavras)
    return result
        

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)