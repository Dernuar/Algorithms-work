import sys

def main():
    data = []
    for line in sys.stdin:
        numbers = list(map(int, line.split()))
        data.extend(numbers)
        if 0 in numbers:
            break
    
    sequence = data[:-1]
    sortsequence = sorted(sequence)
    print(' '.join(map(str, sortsequence)))
    pass

if __name__ == '__main__':
    main()