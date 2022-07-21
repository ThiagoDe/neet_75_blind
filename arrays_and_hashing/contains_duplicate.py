def containsDuplicate(self, nums):
    count_n = {}
    for n in nums:
        if n in count_n:
            return True
        count_n[n] = True

    return False
