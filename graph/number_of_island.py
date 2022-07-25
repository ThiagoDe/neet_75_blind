grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
# Output: 3

def numIsland(grid):
    visited = set()
    res = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited): res += 1

    return res 

def explore(grid, r, c, visited):
    if not inBounds(grid, r, c): return False
    if grid[r][c] == '0': return False 
    pos = (r, c)
    if pos in visited: return False 
    visited.add(pos)

    explore(grid, r + 1, c, visited)
    explore(grid, r - 1, c, visited)
    explore(grid, r , c + 1, visited)
    explore(grid, r, c - 1, visited)
    return True 

def inBounds(grid, r, c):
    rowInbound = 0 <= r < len(grid)
    colInbound = 0 <= c < len(grid[0])

    return rowInbound and colInbound
    
    
print(numIsland(grid))
