import sys
from collections import deque

def main():
    N = int(sys.stdin.readline())
    maze = [sys.stdin.readline().strip() for _ in range(N)]
    row, col = map(int, sys.stdin.readline().split())
    
    row -= 1
    col -= 1
    
    if maze[row][col] == '*':
        print(0)
        return
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    queue = deque()
    queue.append((row, col))
    visited[row][col] = True
    area = 0
    
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        r, c = queue.popleft()
        area += 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and maze[nr][nc] == '.':
                    visited[nr][nc] = True
                    queue.append((nr, nc))   
    print(area)

if __name__ == '__main__':
    main()