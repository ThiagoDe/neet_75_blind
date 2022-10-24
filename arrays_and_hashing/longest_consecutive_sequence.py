nums = [100, 4, 200, 1, 3, 2]
# Output: 4

def longestConsecutive(nums):
    numSet = set(nums) # the set is the most efficent way to check if num exist 
    longest = 0

    for n in nums:
        if (n - 1) not in numSet: # means that this is the first num of a sequense 
            length = 1
            while (n + length) in numSet: # find how many adjents in the sequence 
                length += 1
            longest = max(longest, length)

    return longest 

print(longestConsecutive(nums))


def longestConsecutive(self, nums) -> int:
    numsSet = set(nums)
    longest = 0

    for n in nums:
        if (n - 1) not in numsSet:
            count = 0
            while (n + count) in numsSet:
                count += 1
            longest = max(longest, count)

    return longest
