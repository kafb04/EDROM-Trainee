import textwrap

def wrap(string, max_width):
    texto = textwrap.wrap(string, width=max_width)
    result = '\n'.join(texto)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)