import sys

def main():
    data = []
    for line in sys.stdin:
        numbers = list(map(int, line.split()))
        data.extend(numbers)
        if 0 in numbers:
            break
    
    sequence = data[:-1]
    
    if len(sequence) < 2:
        print(sequence[0])
        return
    
    sortsequence = sorted(sequence)
    print(sortsequence[-2])
    pass

if __name__ == '__main__':
    main()