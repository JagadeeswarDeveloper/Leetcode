class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        max_elem = nums[0]
        for i in range(1,len(nums)):
            current = max(nums[i], nums[i]+current)
            max_elem = max(current, max_elem)
        return max_elem