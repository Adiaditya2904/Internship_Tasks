
def marsExploration(s):
    original = "SOS"
    count = 0

    for i in range(len(s)):
        if s[i] != original[i % 3]:
            count += 1

    return count


s = input().strip()
print(marsExploration(s))
