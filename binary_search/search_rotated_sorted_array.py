nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
# Output: 4

def search(nums, target):
    # l,r = 0, len(nums) - 1

    # while l <= r:
    #     mid = (l + r) // 2
    #     if target == nums[mid]: return mid 

    #     if nums[l] <= nums[mid]: # 4 <= 7
    #         if target > nums[mid] or target < nums[l]:
    #             l = mid + 1
    #         else:
    #             r = mid - 1
    #     else:
    #         if target < nums[mid] or target > nums[r]:
    #             r = mid - 1
    #         else:
    #             l = mid + 1

    # return - 1

        l, r = 0, len(nums) - 1

        while l <= r: # "=" if nums length 1 eg: [8]
            mid = (l + r) // 2  # increase or decrease the pivot index on the original list
            
            if nums[mid] == target: # base case 
                return mid
            
            if nums[mid] >= nums[l]: # check both sides // compare l and mid not target
                # left side
                if target > nums[mid] or target < nums[l]: # if target is not in this range
                    l = mid + 1 # go check the right side
                else:
                    r = mid - 1 # stay on the left side
            else:
                # right side whe mid is smaller than l
                if target < nums[mid] or target > nums[r]: # if target is not in the range mid to r
                    r = mid - 1 # go back and check the left side
                else:
                    l = mid + 1 # keep searching on the right side
                    
        return - 1

print(search(nums, target))


class Solution:
    def search(self, nums, target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:

            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # left sorted
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1

        return - 1
