# s = "ABAB"
# k = 2
# # Output: 4
# def characterReplacement(s, k):
#     count = {} # A:1
#     res = 0

#     l = 0
#     for r in range(len(s)): # range starts at 0
#         count[s[r]] = 1 + count.get(s[r], 0) # use s[r] track num chars 
#         while (r - l + 1) - max(count.values()) > k: # if k not enought to replace char
#             count[s[l]] -= 1 #update count of chars when swiching l += 1
#             l += 1
        
#         res = max(res, r - l + 1)

#     return res 

# print(characterReplacement(s, k))

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l = 0
        res = 0

        maxFreq = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxFreq = max(maxFreq, count[s[r]])

            while (r - l + 1) - maxFreq > k:
                count[s[l]] -= 1
                l += 1

            res = max(res, (r - l + 1))

        return res
