from collections import defaultdict
# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.


# Example 1:

# Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
# Example 2:

# Input: strs = [""]
# Output: [[""]]
# Example 3:

# Input: strs = ["a"]
# Output: [["a"]]

def groupAnagrams(strs):
    res = defaultdict(list) # to deal w edge case the dict = { key: [] } list default
    # for s in strs:
    #     # print(s)
    #     sortedS = ''.join(sorted(s))
    #     # print(sortedS)
    #     if sortedS not in res:
    #         res[sortedS] = [s]
    #     else:
    #         res[sortedS].append(s)
    # return res.values()
    for s in strs: #O(m * n)
        count = [0] * 26 # count the char a-z (122 - 97)
        # [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        for c in s:
            count[ord(c) - ord('a')] += 1
            # print(ord(c))
            # print(ord('a'))
            # print(ord('z'))
            # print(count)
            print(tuple(count))
        res[tuple(count)].append(s) # in python list can not be keys
        print(count)
    return res.values()

strs = ["eat","tea","tan","ate","nat","bat"]

print(groupAnagrams(strs))