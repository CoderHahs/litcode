# 829. Consecutive Numbers Sum
# Hard

# 345

# 465

# Add to List

# Share
# Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

# Example 1:

# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# Example 2:

# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# Example 3:

# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# Note: 1 <= N <= 10 ^ 9.


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        count = 1
        max = int((sqrt(1 + (8 * N)) - 1) / 2)
        for i in range(2, max + 1):
            if i % 2 == 1 and N % i == 0:
                count += 1
            elif i % 2 == 0 and N % i == i / 2:
                count += 1
        return count
