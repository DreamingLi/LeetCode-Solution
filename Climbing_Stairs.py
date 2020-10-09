
# 70. Climbing Stairs

# # This is a dynamic problem such as fib, so it has optimal substructures. My solution is to save the results for reuse to improve the calculating speed.

class Solution:
    cache_dic = {"1":1,"2":2,"3":3,"4":5,"5":8,"6":13} # provide a basic cache
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if str(n) in self.cache_dic: # if the result has been calculated, just return the result
            return self.cache_dic[str(n)]
        else:
            self.cache_dic[str(n)] = self.climbStairs(n-1)+self.climbStairs(n-2) # save the new result for reuse
            return self.cache_dic.get(str(n))
        
# Runtime: 20 ms, faster than 98.54% of Python3 online submissions for Climbing Stairs.
# Memory Usage: 14.1 MB, less than 99.98% of Python3 online submissions for Climbing Stairs.
