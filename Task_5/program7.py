def average(array):
    # your code goes here
    distinct = set(arr)
    return round(sum(distinct) / len(distinct), 3)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
