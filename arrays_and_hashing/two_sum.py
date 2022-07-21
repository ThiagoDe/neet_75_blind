def twoSum(self, nums: List[int], target: int) -> List[int]:
    indices = {}
    for i in range(len(nums)):
        dif = target - nums[i]
        if dif in indices:
            return [indices[dif], i]
        indices[nums[i]] = i
