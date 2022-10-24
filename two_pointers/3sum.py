# nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0]
# nums = [0, -1, 1]
nums = [-1, 0, 1, 2, -1, -4]

# Output: [[-1, -1, 2], [-1, 0, 1]]

def threeSum(nums):
    # res = []
    # sortedNum = sorted(nums)
    # #[-4, -1, -1, 0, 1, 2]
    # for i in range(len(sortedNum) - 2): # 0..3
        
    #     target = sortedNum[i] # -4
    #     l, r = i + 1, len(sortedNum) -1
    #     while l < r:
    #         sumN = target + sortedNum[l] + sortedNum[r]
    #         if sumN == 0:
    #             if [target, sortedNum[l], sortedNum[r]] not in res:
    #                 res.append([target, sortedNum[l], sortedNum[r]])
    #             r -= 1
    #             l += 1
    #         elif sumN > 0:
    #             r -= 1
    #         else:
    #             l += 1

    # return res
    res = []
    nums.sort()

    for i, n in enumerate(nums):
        if i > 0 and n == nums[i - 1]:
            continue

        l, r = i + 1, len(nums) - 1
        while l < r:
            threeSum = n + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([n, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l - 1] and l < r:
                    l += 1

    return res

print(threeSum(nums))


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         res = []
#         nums.sort()
#         print(nums)
#         for i, a in enumerate(nums):
#             if i > 0 and a == nums[i - 1]:
#                 continue

#             l, r = i + 1, len(nums) - 1

#             # two sum
#             while l < r:
#                 total = a + nums[l] + nums[r]
#                 if total > 0:
#                     r -= 1
#                 elif total < 0:
#                     l += 1
#                 else:
#                     res.append([a, nums[l], nums[r]])
#                     l += 1
#                     while nums[l] == nums[l - 1] and l < r:
#                         l += 1

#         return res
