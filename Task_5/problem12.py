
s = input()

for word in s.split(' '):
    if word:
        s = s.replace(word, word[0].upper() + word[1:], 1)

print(s)
