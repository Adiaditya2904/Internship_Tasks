n = int(input())
english = set(map(int, input().split()))

m = int(input())
french = set(map(int, input().split()))

result = english.difference(french)

print(len(result))
