class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)
output:
nums =
[1,3,5,6]
target =
5
Output
2
Expected
2