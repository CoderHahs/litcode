# We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
#
# Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
# Example:
# Input: 28
# Output: True
# Explanation: 28 = 1 + 2 + 4 + 7 + 14
# Note: The input number n will not exceed 100,000,000. (1e8)



import math
class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        sum = 1
        print(math.floor(int((num**2)**0.25)))
        for i in range(2, math.floor(int((num**2)**0.25))+1):
            if (num%i == 0):
                #print (i,num/i)
                sum += i
                sum += (num/i)
        if (sum == num and num != 1):
            return True
        else:
            return False
