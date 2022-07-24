nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# Output: 4

def search(nums, target):
    l,r = 0, len(nums) - 1

    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]: return mid 

        if nums[l] <= nums[mid]: # 4 <= 7
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1

    return - 1

print(search(nums, target))