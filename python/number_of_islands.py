# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
# Example 2:
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def visit_neighbours(i, j):
            to_visit = [(i,j)]
            for point in to_visit:
                # print(point)
                if (grid[point[0]][point[1]] == "1"):
                    visited.add(point)
                    if (point[0]-1 >= 0):
                        if ((point[0]-1, point[1]) not in visited):
                            to_visit.append((point[0]-1, point[1]))
                    if (point[0]+1 < len(grid)):
                        if ((point[0]+1, point[1]) not in visited):
                            to_visit.append((point[0]+1, point[1]))
                    if (point[1]-1 >= 0):
                        if ((point[0], point[1]-1) not in visited):
                            to_visit.append((point[0], point[1]-1))
                    if (point[1]+1 < len(grid[point[0]])):
                        if ((point[0], point[1]+1) not in visited):
                            to_visit.append((point[0], point[1]+1))
        islands = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                # print(visited)
                if ((i, j) not in visited and grid[i][j] == "1"):
                    visit_neighbours(i,j)
                    islands += 1

        return islands
