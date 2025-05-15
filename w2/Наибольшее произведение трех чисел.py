import sys

def solution(arr):
    arr.sort()
    n = len(arr)
    option1 = arr[-1] * arr[-2] * arr[-3]
    option2 = arr[0] * arr[1] * arr[-1]
    
    if option1 > option2:
        return arr[-3], arr[-2], arr[-1]
    else:
        return arr[0], arr[1], arr[-1]

def main():
    data = list(map(int, sys.stdin.readline().split()))
    result = solution(data)
    print(' '.join(map(str, result)))

if __name__ == '__main__':
    main()