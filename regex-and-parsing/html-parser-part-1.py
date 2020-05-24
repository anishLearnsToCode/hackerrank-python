# https://www.hackerrank.com/challenges/html-parser-part-1/problem

from html.parser import HTMLParser


# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        self.handle_attrs(attrs)

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        self.handle_attrs(attrs)

    def handle_attrs(self, attrs):
        for attribute in attrs:
            print('->', attribute[0], '>', attribute[1])


parser = MyHTMLParser()

n = int(input())
for _ in range(n):
    html = input()
    parser.feed(html)
