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

    tree = {}
    for num in data:
        node = tree
        while True:
            if 'value' not in node:
                node.update({'value': num, 'left': {}, 'right': {}})
                break
            elif num < node['value']:
                node = node['left']
            elif num > node['value']:
                node = node['right']
            else:
                break

    leaves = []
    stack = [tree]
    while stack:
        node = stack.pop()
        if not node['left'] and not node['right']:
            leaves.append(node['value'])
        if node['right']:
            stack.append(node['right'])
        if node['left']:
            stack.append(node['left'])

    leaves.sort()
    print(' '.join(map(str, leaves)))
    pass

if __name__ == '__main__':
    main()