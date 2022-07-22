class Solution:
    def search(self, nums: list[int], target: int) -> int:
        # l, r = 0, len(nums) - 1
        mid = len(nums) // 2
        if not nums:
            return -1
        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            return self.search(nums[:mid], target)
        else:
            memo = self.search(nums[mid + 1:], target)
            if memo == -1:
                return -1
            else:
                return memo + mid + 1


# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1
