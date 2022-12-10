# pylint: disable-all

f = open('input.txt', 'r')

matrix = []
rows = 0
cols = 0

def tree_visible(row, col):
    prev_max_height = 0
    # left to right
    for i in range(col):
        if matrix[row][i] > prev_max_height:
            prev_max_height = matrix[row][i]
    if matrix[row][col] > prev_max_height:
        return True
    
    prev_max_height = 0
    # right to left
    for i in range(cols - 1, col, -1):
        if matrix[row][i] > prev_max_height:
            prev_max_height = matrix[row][i]
    if matrix[row][col] > prev_max_height:
        return True
    
    prev_max_height = 0
    # top to bottom
    for i in range(row):
        if matrix[i][col] > prev_max_height:
            prev_max_height = matrix[i][col]
    if matrix[row][col] > prev_max_height:
        return True
    
    prev_max_height = 0
    # from bottom to top
    for i in range(rows-1, row, -1):
        if matrix[i][col] > prev_max_height:
            prev_max_height = matrix[i][col]
    if matrix[row][col] > prev_max_height:
        return True

def calc_score(row, col):
    top_score = 0
    bottom_score = 0
    left_score = 0
    right_score = 0

    # left to right
    for i in range(col + 1, cols):
        if matrix[row][col] > matrix[row][i]:
            right_score += 1
        else:
            right_score += 1
            break
    
    # right to left
    for i in range(col-1, -1, -1):
        if matrix[row][col] > matrix[row][i]:
            left_score += 1
        else:
            left_score += 1
            break
    
    # to top
    for i in range(row-1, -1, -1):
        if matrix[row][col] > matrix[i][col]:
            top_score += 1
        else:
            top_score += 1
            break

    # to bottom 
    for i in range(row+1, rows):
        if matrix[row][col] > matrix[i][col]:
            bottom_score += 1
        else:
            bottom_score += 1
            break

    return bottom_score * top_score * left_score * right_score


for line in f:
    line = line.strip('\n')
    matrix.append((list(int(x) for x in line)))
rows = len(matrix)
cols = len (matrix[0])

edge_trees = (rows*2) + ((cols - 2)*2)
visible_tree_count = edge_trees

for row in range(1, rows - 1):
    for col in range(1, cols - 1):
        if tree_visible(row, col):
            visible_tree_count += 1

highest_score = 0
for row in range(rows):
    for col in range(cols):
        score = calc_score(row, col)
        if score > highest_score:
            highest_score = score

print(f"Part 1: {visible_tree_count}")
print(f"part 2highest_score)