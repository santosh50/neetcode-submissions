class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            target = -nums[i]
            while l < r:
                total = nums[l] + nums[r]
                if total == target:
                    triple = (nums[i], nums[l], nums[r])
                    if triple not in seen:
                        res.append(list(triple))
                        seen.add(triple)
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        
        return res

        