import sys

def main():
    data = []
    for line in sys.stdin:
        nums = list(map(int, line.split()))
        for num in nums:
            if num == 0:
                break
            data.append(num)
        if 0 in nums:
            break

    root = None
    tree = {}
    output = []

    for num in data:
        depth = 1
        node = tree
        inserted = False
        
        while True:
            if 'value' not in node:
                node.update({'value': num, 'left': {}, 'right': {}})
                output.append(str(depth))
                inserted = True
                break
            elif num < node['value']:
                node = node['left']
                depth += 1
            elif num > node['value']:
                node = node['right']
                depth += 1
            else:
                break
        
    print(' '.join(output))
    pass

if __name__ == '__main__':
    main()