class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        res = [1] * size
        for i in range(1, size):
            res[i] = res[i-1] * nums[i-1]
        postProd = 1
        for i in range(size-1, -1, -1):
            res[i] = postProd * res[i]
            postProd *= nums[i]
        return res
            

        