class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices = {}
        for i in range(len(nums)):
            dif = target - nums[i]
            if dif in indices:
                return [indices[dif], i]
            indices[nums[i]] = i
