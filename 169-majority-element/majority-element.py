class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        max_count = 0
        temp = nums[0]
        for i in range(len(nums)):
            if max_count == 0:
                temp = nums[i]
            if nums[i] == temp:
                max_count += 1 
            else:
                max_count -= 1
            
        return temp

        

                
                