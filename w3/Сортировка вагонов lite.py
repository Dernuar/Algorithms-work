import sys

def main():
    input = sys.stdin.read
    data = list(map(int, input().split()))
    N = data[0]
    wagons = data[1:]
    stack = []
    current = 1

    for wagon in wagons:
        stack.append(wagon)
        while stack and stack[-1] == current:
            stack.pop()
            current += 1

    if current == N + 1:
        print("YES")
    else:
        print("NO")
    pass


if __name__ == '__main__':
    main()