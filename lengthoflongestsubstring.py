class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s) == 0):
            return 0
        occurence = {}
        l = 0
        r = 0
        longest = 0
        while r < len(s):
            if(s[r] in occurence.keys()):
                l = max(l, occurence[s[r]] + 1)
            occurence[s[r]] = r
            longest = max(longest, (r-l)+1)
            r += 1
        return longest
        