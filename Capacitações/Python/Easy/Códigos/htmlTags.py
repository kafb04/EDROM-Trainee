from html.parser import HTMLParser

class MeuParserHTML(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

if __name__ == '__main__':
    n = int(input())
    codigo_html = '\n'.join(input() for i in range(n))
    parser = MeuParserHTML()
    parser.feed(codigo_html)
