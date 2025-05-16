import sys

def main():
    tokens = sys.stdin.read().strip().split()
    stack = []

    for token in tokens:
        if token.isdigit():
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
    print(stack[0])

    pass


if __name__ == '__main__':
    main()