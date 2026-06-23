class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        curr_min = nums[0]
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            curr_min = min(nums[m], curr_min)
            if nums[m] < nums[0]:
                r = m - 1
            else:
                l = m + 1
        return curr_min
