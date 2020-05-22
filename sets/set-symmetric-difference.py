# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

int(input())
english_subscriptions = set(map(int, input().split()))

int(input())
french_subscriptions = set(map(int, input().split()))

all_subscriptions = english_subscriptions.symmetric_difference(french_subscriptions)
print(len(all_subscriptions))
