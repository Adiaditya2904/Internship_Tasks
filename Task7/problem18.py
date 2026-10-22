def weightedUniformStrings(s, queries):
    weights = set()
    curre
  nt_weight = 0
    previous_char = ''

    for char in s:
        weight = ord(char) - ord('a') + 1

        if char == previous_char:
            current_weight += weight
        else:
            current_weight = weight

        weights.add(current_weight)
        previous_char = char

    result = []

    for q in queries:
        if q in weights:
            result.append("Yes")
        else:
            result.append("No")

    return result
