class Solution:
    
    cache_dic = {"1":1,"2":2,"3":3,"4":5,"5":8,"6":13}

    def climbStairs(self, n: int) -> int:

        if n == 0:
            return 0
        if str(n) in self.cache_dic:
            return self.cache_dic[str(n)]
        else:
            x = self.climbStairs(n-1)
            y = self.climbStairs(n-2)
            self.cache_dic[str(n)] = x+y
            return self.cache_dic.get(str(n))
        
