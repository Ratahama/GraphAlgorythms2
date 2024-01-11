def dfs(curr_node, row, col, matrix, visited, result):
    if row < 0 or col < 0 or row >= len(matrix) or col >= len(matrix[0]):
        return 0
    if visited[row][col]:
        return 0
    if curr_node != matrix[row][col]:
        return 0

    visited[row][col] = True
    dfs(curr_node, row - 1, col, matrix, visited, result)
    dfs(curr_node, row + 1, col, matrix, visited, result)
    dfs(curr_node, row, col - 1, matrix, visited, result)
    dfs(curr_node, row, col + 1, matrix, visited, result)
    return 1



rows = int(input())
cols = int(input())
matrix = [list(input()) for _ in range(rows)]
visited = [[False] * cols for _ in range(rows)]
# directions = {'here': (0, 0), 'up': (-1, 0), 'down': (1, 0), 'right': (0, 1), 'left': (0, -1)}

result = {}

total_areas = 0
for row in range(rows):
    for col in range(cols):
        curr_node = matrix[row][col]
        value = dfs(curr_node, row, col, matrix, visited, result)
        total_areas += value

        if curr_node not in result:
            result[curr_node] = 0
        result[curr_node] += value


print(f'Areas: {total_areas}')
[print(f"Letter '{k}' -> {v}") for k, v in sorted(result.items())]







# # INPUT1:
# 6
# 8
# aacccaac
# baaaaccc
# baabaccc
# bbdaaccc
# ccdccccc
# ccdccccc
#
# # take the last empty line too, saves you an enter press
# # OUTPUT1:
# Areas: 8
# Letter 'a' -> 2
# Letter 'b' -> 2
# Letter 'c' -> 3
# Letter 'd' -> 1

# # INPUT2:
# 3
# 3
# aaa
# aaa
# aaa
#
# # take the last empty line too, saves you an enter press
# # OUTPUT2:
# Areas: 1
# Letter 'a' -> 1


# # INPUT3:
# 5
# 9
# asssaadas
# adsdasdad
# sdsdadsas
# sdasdsdsa
# ssssasddd
#
# # take the last empty line too, saves you an enter press
# # OUTPUT3:
# Areas: 21
# Letter 'a' -> 6
# Letter 'd' -> 7
# Letter 's' -> 8


