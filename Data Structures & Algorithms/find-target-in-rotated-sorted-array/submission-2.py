class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            if nums[m] >= nums[0]:
                if target > nums[m]:
                    l = m + 1
                elif target < nums[0]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m]:
                    r = m - 1
                elif target > nums[-1]:
                    r = m - 1
                else:
                    l = m + 1
        return -1

        