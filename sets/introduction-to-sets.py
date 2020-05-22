n = int(input())
tokens = map(int , input().split())
plants = set(tokens)
print(sum(plants) / len(plants))
