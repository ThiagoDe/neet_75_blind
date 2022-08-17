nums = [3, 4, 5, 1, 2]
# Output: 1
# Thia challange need more love

def findMin(nums):
    res = nums[0]
    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l] < nums[r]: # this case means that the roted array is sorted
            res = min(res, nums[l])
            break 

        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]: # if mid >= l means leftside is sorted the min is gonna be at the rightside
            l = m + 1 # sets the search on rightside
        else:
            r = m - 1 # keep checking on the left side

    return res

print(findMin(nums))