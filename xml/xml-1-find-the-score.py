# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem

import xml.etree.ElementTree as etree


def get_attr_number(node):
    result = 0
    for child in node:
        result += get_attr_number(child)
    return result + len(node.attrib)


if __name__ == '__main__':
    xml = ''
    for _ in range(int(input())):
        xml += input()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()

    print(get_attr_number(root))
