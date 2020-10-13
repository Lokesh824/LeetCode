class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ O(n2) approach
        for i in range(0, len(nums)):
            notofind = (target - nums[i])
            for j in range(i+1, len(nums)):
                if(nums[j] == notofind):
                    return [i,j]"""
        """Optimal Soln with O(n) TC and O(n) SC"""
        hs = {}
        for i in range(0, len(nums)):
            numtofind = target - nums[i]
            if(numtofind in hs.keys()):
                return [hs[numtofind], i]
            else:
                hs[nums[i]] = i