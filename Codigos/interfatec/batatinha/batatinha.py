n = int(input())
start_row, start_col = map(int, input().split())
target_row, target_col = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(input()))

def find_min_path(curr_row, curr_col, curr_path) -> list:
    min_path = []
    min_size = 1000000
    
    if curr_row == target_row and curr_col == target_col:
        return curr_path
    
    for move_row,move_col in [(-1,0),(0,1),(1,0),(0,-1)]:
        next_row = curr_row+move_row
        next_col = curr_col+move_col

        if 0 <= next_row-1 < n and 0 <= next_col-1 < n and maze[next_row-1][next_col-1] == '1':
            maze[next_row-1][next_col-1] = '0'

            result = find_min_path(next_row,next_col,curr_path+[(next_row,next_col)])

            maze[next_row-1][next_col-1] = '1'

            if 0 < len(result) < min_size:
                min_path = result
                min_size = len(min_path) 

    return min_path

result = find_min_path(start_row,start_col,[(start_row,start_col)])

for row,col in result:
    print(row,col)