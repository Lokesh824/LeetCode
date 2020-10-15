class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        print(nums)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                numstofind = target - (nums[i] + nums[j])
                l = j + 1
                r = len(nums) - 1
                while(l<r):
                    twosum = nums[l]+nums[r]
                    if(numstofind > twosum):
                        l += 1
                    elif(numstofind < twosum):
                        r -= 1
                    else:
                        left = nums[l]
                        right = nums[r]
                        res.append([nums[i], nums[j], left, right])
                        while(l < r and nums[l] == left):
                       
                            l += 1
                        while(l<r and nums[r] == right):
        
                            r -= 1
                                
                        
        res1 = list(set(tuple(sorted(sub)) for sub in res))                           
        return res1         
        