# 3. Longest Substring Without Repeating Characters

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ret=""
        for i in s:
            ret+=i
            if len(ret)!=len(set(ret)):
                ret=ret[1:]
        return len(ret)
        
# Runtime: 136 ms, faster than 23.21% of Python3 online submissions for Longest Substring Without Repeating Characters.       
# Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Longest Substring Without Repeating Characters.

# 解题思路：
# 1. 拿到第一位的元素，尝试看他的满足要求的字串长度是多少，假如是3，那么就是如果用第一个元素作为开头，那么我们能拿到最长字串为3。拿第二位的元素去尝试看它满足要求的子串长度是多少，假如是5，那么
# 我们就知道，第二位要比第一位长，依次类推，我们就能找到这个字符串中最长的，并且不重复的子串。
# 2. 有了解题思路之后，下一步是优化。 假如我们第一位字母，他的最长长度是。我们换到第二位的话，其实我们第一位字母的最长子串是包括一部分第二位的子串的，假如我们拿到的字符串时abcabc,那么第一位a
# 开始的话，就是abc。如果b开始的话，是bca。 这个bc是包括在第一个子串中的。因此 如果能不去计算重复的部分，或者不多份存储重复的部分的话，就可以节约时间和空间。
# 3. 按照这个思路来解题的话，我们可以不停的拼一个字符串，一旦发现重复的，就表示最开始的一位来做第一位字母的话，已经有了最长的长度。 我们就把第一位删掉，但是重复的还是保留在我们的字符串中
# 通过这种方式来保存我们的最长长度
