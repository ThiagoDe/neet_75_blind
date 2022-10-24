# nums = [1,2,3,4]
# # Output: [24,12,8,6]
# def productExceptSelf(nums):
#     res = [1] * len(nums) # [1,1,1,1]

#     prefix = 1
#     for i in range(len(nums)): # [1, 1, 2, 6] (24) full length so the last operation computes 
#         res[i] = prefix
#         prefix *= nums[i]

#     postfix = 1
#     for i in range(len(nums) -1, -1, -1): # [24,12,8,6]
#         res[i] *= postfix
#         postfix *= nums[i]

#     return res  

# print(productExceptSelf(nums))

class Solution:
    def productExceptSelf(self, nums):
        # create a res list to store all the products
        res = [1] * len(nums)

        # set prefix to 1
        prefix = 1

        # iterate nums
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
