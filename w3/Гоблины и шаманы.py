import sys
from collections import deque

def main():
    input = sys.stdin.read
    data = input().splitlines()
    n = int(data[0])
    left = deque()
    right = deque()
    result = []
    
    for line in data[1:]:
        if line[0] == '+':
            _, i = line.split()
            right.append(i)
        elif line[0] == '*':
            _, i = line.split()
            left.append(i)
        else:
            result.append(left.popleft())

        if len(left) < len(right):
            left.append(right.popleft())
        elif len(left) > len(right) + 1:
            right.appendleft(left.pop())
    
    print('\n'.join(result))
    pass

if __name__ == '__main__':
    main()