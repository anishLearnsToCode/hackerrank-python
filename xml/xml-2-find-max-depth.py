# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    for child in elem:
        maxdepth = max(maxdepth, depth(child, level + 1))

    maxdepth = max(maxdepth, level + 1)
    return maxdepth

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)