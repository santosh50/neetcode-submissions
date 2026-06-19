class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    triple = [nums[i], nums[l], nums[r]]
                    if triple not in res:
                        res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        
        return res

        