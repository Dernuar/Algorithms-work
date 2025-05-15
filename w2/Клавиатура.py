def main():

    n = int(sys.stdin.readline())
    st = list(map(int, sys.stdin.readline().split()))
    k = int(sys.stdin.readline())
    presses = list(map(int, sys.stdin.readline().split()))

    count = [0] * n
    
    for key in presses:
        count[key-1] += 1

    result = []
    for i in range(n):
        if count[i] > st[i]:
            result.append("YES")
        else:
            result.append("NO")

    print('\n'.join(result))

if __name__ == '__main__':
    main()