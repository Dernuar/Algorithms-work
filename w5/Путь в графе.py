import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    adj = [[] for _ in range(N+1)]
    
    for i in range(1, N+1):
        row = list(map(int, sys.stdin.readline().split()))
        for j in range(N):
            if row[j] == 1:
                adj[i].append(j+1)
    
    s, e = map(int, sys.stdin.readline().split())
    
    if s == e:
        print(0)
        return
    
    visited = [False] * (N+1)
    parent = [0] * (N+1)
    queue = deque()
    queue.append(s)
    visited[s] = True
    found = False
    
    while queue:
        current = queue.popleft()
        
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current
                queue.append(neighbor)
                
                if neighbor == e:
                    found = True
                    queue = deque()
                    break
    
    if not found:
        print(-1)
    else:

        path = []
        node = e
        while node != s:
            path.append(node)
            node = parent[node]
        path.append(s)
        path.reverse()
        
        print(len(path)-1)
        print(' '.join(map(str, path)))

if __name__ == '__main__':
    main()