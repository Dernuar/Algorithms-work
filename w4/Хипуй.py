import sys

def main():
    heap = []
    output = []
    
    for line in sys.stdin:
        if not line.strip():
            continue
            
        parts = line.split()
        if parts[0] == '0':
            num = int(parts[1])
            heap.append(num)
            i = len(heap) - 1
            while i > 0:
                parent = (i - 1) // 2
                if heap[i] > heap[parent]:
                    heap[i], heap[parent] = heap[parent], heap[i]
                    i = parent
                else:
                    break
        elif parts[0] == '1':
            if not heap:
                continue
                
            output.append(str(heap[0]))
            
            heap[0] = heap[-1]
            heap.pop()
            
            i = 0
            n = len(heap)
            while True:
                left = 2 * i + 1
                right = 2 * i + 2
                largest = i
                
                if left < n and heap[left] > heap[largest]:
                    largest = left
                if right < n and heap[right] > heap[largest]:
                    largest = right
                    
                if largest != i:
                    heap[i], heap[largest] = heap[largest], heap[i]
                    i = largest
                else:
                    break
    
    print('\n'.join(output))

if __name__ == '__main__':
    main()