class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_size = len(nums)+1
        l = 0 
        r = 0 
        sum1 = 0
        while r<len(nums):
            sum1+=nums[r]
            while sum1 >= target:
                if (r - l) + 1 < min_size:
                    min_size = (r - l) + 1
                sum1 -= nums[l]
                l+=1
            r+=1
        if min_size == len(nums)+1:
            return 0 

        return min_size 
        