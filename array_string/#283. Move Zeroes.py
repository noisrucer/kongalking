class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        
        num = 0

        for j in range(len(nums)):
            if nums[j] != 0:
                num = nums[i]
                nums[i] = nums[j]
                nums[j] = num
                i += 1