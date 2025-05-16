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
            if not node:
                tree.update({'value': num, 'left': {}, 'right': {}, 'height': 1})
                break
            elif num < node['value']:
                if not node['left']:
                    node['left'] = {'value': num, 'left': {}, 'right': {}, 'height': 1}
                    break
                node = node['left']
            elif num > node['value']:
                if not node['right']:
                    node['right'] = {'value': num, 'left': {}, 'right': {}, 'height': 1}
                    break
                node = node['right']
            else:
                break

    def check_balance(node):
        if not node or not node.get('value'):
            return (True, 0)
        
        left_balance, left_height = check_balance(node.get('left', {}))
        right_balance, right_height = check_balance(node.get('right', {}))
        
        balance = (abs(left_height - right_height)) <= 1 and left_balance and right_balance
        current_height = max(left_height, right_height) + 1
        
        return (balance, current_height)

    is_balance, _ = check_balance(tree)
    print("YES" if is_balance else "NO")
    pass

if __name__ == '__main__':
    main()