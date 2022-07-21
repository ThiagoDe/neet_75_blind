def containsDuplicate(self, nums):
    count_n = {}
    for n in nums:
        if n in count_n:
            return True
        count_n[n] = True

    return False


# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         hashset = set()

#         for n in nums:
#             if n in hashset:
#                 return True
#             hashset.add(n)
#         return False
