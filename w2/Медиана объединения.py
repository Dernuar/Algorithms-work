import sys

def main():
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    L = int(data[1])

    sequences = []
    index = 2
    for _ in range(N):
        seq = list(map(int, data[index:index + L]))
        sequences.append(seq)
        index += L

    results = []

    for i in range(N):
        for j in range(i + 1, N):
            merged = sorted(sequences[i] + sequences[j])
            median = merged[L - 1]
            results.append(str(median))

    print('\n'.join(results))


if __name__ == '__main__':
    main()