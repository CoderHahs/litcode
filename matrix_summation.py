# An m x n matrix called before was used to create a new m x n matrix called after in the following way:

# For all x from 0 to m - 1 and y from 0 to n - 1 the following function was applied:

# void modify(vector<vector<int> >& before, vector<vector<int> >& after, int x, int y) {
# 	int s = 0;
# 	for (int i = 0; i <= x; ++i) {
# 		for (int j = 0; j <= y; ++j) {
# 			s += before[x][y];
# 		}
# 	}

# 	after[x][y] = s;
# }
# Given only the matrix after, find the before matrix.


def findBeforeMatrix(after):
    before_matrix = after

    for i in range(len(after[0])):
        for j in range(len(after)):
            if i == 0:
                before_matrix[i][j] = after[i][j] - before_matrix[i][j - 1]
            elif j == 0:
                before_matrix[i][j] = after[i][j] - before_matrix[i - 1][j]
            else:
                before_matrix[i][j] = (
                    after[i][j]
                    - before_matrix[i - 1][j]
                    - before_matrix[i][j - 1]
                    - before_matrix[i - 1][j - 1]
                )

    return before_matrix
