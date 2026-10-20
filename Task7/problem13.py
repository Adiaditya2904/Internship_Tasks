
#!/bin/python3

import os
import sys
from collections import Counter

def isValid(s):
    char_count = Counter(s)
    freq_count = Counter(char_count.values())

    if len(freq_count) == 1:
        return "YES"

    if len(freq_count) > 2:
        return "NO"

    freq1, freq2 = freq_count.keys()
    count1, count2 = freq_count.values()

    if (freq1 == 1 and count1 == 1) or (freq2 == 1 and count2 == 1):
        return "YES"

    if abs(freq1 - freq2) == 1:
        if freq1 > freq2 and count1 == 1:
            return "YES"
        if freq2 > freq1 and count2 == 1:
            return "YES"

    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()
    result = isValid(s)

    fptr.write(result + '\n')
    fptr.close()
