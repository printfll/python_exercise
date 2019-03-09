import sys
max_num = 0
max_path = []
def dfs(grid, visit, i, j):
    global max_num, max_path
    visit[i][j]=True
    dire = [[1,0], [-1,0], [0,1], [0,-1]]
    gold = grid[i][j]
    res = []
    for x, y in dire:
        new_i, new_j = x+i, y+j
        if 0<=new_i<len(grid) and 0<=new_j<len(grid[0]) and \
            grid[new_i][new_j] and not visit[new_i][new_j]:
            res.append(dfs(grid, visit, new_i, new_j))
    if res:
        res.sort(key=lambda x:x[0])
        cur_gold = gold+res[-1][0]+res[-2][0] if len(res)>1 else 0
        if cur_gold > max_num:
            max_path=res[-1][1][:]
            max_path.append([i,j])
            if len(res)>1:
                max_path.extend(res[-2][1])
            max_num = cur_gold
        cur_path = res[-1][1][:]
        cur_path.append([i,j])
        return gold+res[-1][0], cur_path
    return gold, [[i,j]]
    
def max_gold(grid):
    visit = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]>0 and not visit[i][j]:
                dfs(grid, visit, i, j)
    return max_num, max_path

grid = [[0, 0, 1, 2, 3, 0],
        [1, 0, 4, 0, 2, 5],
        [0, 0, 5, 0, 1, 0],
        [0, 2, 0, 1, 0, 5]]
print(max_gold(grid))
#(22, [[1, 5], [1, 4], [0, 4], [0, 3], [0, 2], [2, 2], [1, 2]])