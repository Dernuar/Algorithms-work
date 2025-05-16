import sys

def main():
    s = sys.stdin.readline().strip()

    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack or stack[-1] != pairs[char]:
                print("no")
                return
            stack.pop()

    if not stack:
        print("yes")
    else:
        print("no")
    pass


if __name__ == '__main__':
    main()