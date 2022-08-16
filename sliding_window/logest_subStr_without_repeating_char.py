s = "abcabcbb"
s = "dvdf"

def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet: # d
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r]) # add (set)
        res = max(res, (r - l + 1)) # 0 - 0 + 1, 1 - 0 + 1, 2 - 1 + 1, 3 - 1 + 1
    return res # 1, 2, 2, 
        



print(lengthOfLongestSubstring(s))
