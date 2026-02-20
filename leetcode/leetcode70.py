class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        
        a = 1
        b = 2
        
        for i in range(3, n + 1):
            temp = a + b
            a = b
            b = temp
        
        return b