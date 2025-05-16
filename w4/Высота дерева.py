import sys

def main():
    nums = []
    for line in sys.stdin:
        for num in map(int, line.split()):
            if num == 0:
                break
            nums.append(num)
        else:
            continue
        break

    tree = {}
    height = 0

    for num in nums:
        curheight = 1
        node = tree
        while True:
            if 'value' not in node:
                node.update({'value': num, 'left': {}, 'right': {}, 'depth': curheight})
                if curheight > height:
                    height = curheight
                break
            elif num < node['value']:
                node = node['left']
                curheight += 1
            elif num > node['value']:
                node = node['right']
                curheight += 1
            else:
                break

    print(height)
    pass

if __name__ == '__main__':
    main()