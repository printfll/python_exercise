import sys
def l1_dis(x_pos, i, j):
    return abs(x_pos[0]-i)+abs(x_pos[1]-j)

def binary_search(row, target):
    if target < row[0]:
        return 0
    if target > row[-1]:
        return len(row)
    i, j = 0, len(row)-1
    while i<j:
        mid = (i+1)/2
        if row[mid]==target:
            return mid
        elif row[mid]<target:
            i = mid+1
        else:
            j = mid-1
    return i
    
def shortest_dis(grid):
    x_list = []
    y_grid = []
    for i in range(len(grid)):
        y_grid.append([])
        for j in range(len(grid[0])):
            if grid[i][j] == "X":
                x_list.append([i,j])
            elif grid[i][j] == "Y":
                y_grid[-1].append(j)
    short_dis = sys.maxsize
    for x in x_list:
        for row, y_row in enumerate(y_grid):
            if y_row:
                search_point = binary_search(y_row, x[1])
                cur_dis = l1_dis(x, row, y_row[search_point])
                prev_dis = l1_dis(x, row, y_row[search_point-1]) if search_point>0 else sys.maxsize
                aft_dis = l1_dis(x, row, y_row[search_point+1]) if search_point<len(y_row)-1 else sys.maxsize
                short_dis = min(cur_dis, prev_dis, aft_dis, short_dis)
    return short_dis

input = [["*","*","*","*","*"],
         ["*","X","X","*","*"],
         ["*","*","*","Y","*"],
         ["X","*","*","Y","*"]]
print(shortest_dis(input))

