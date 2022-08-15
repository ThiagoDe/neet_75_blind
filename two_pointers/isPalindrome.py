s = "A man, a plan, a canal: Panama"


class Solution: # contant memory O(n)

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        # print(self.isAlpha(s[j]))
        # print(self.isAlpha(s[i]))
        while i < j:
            while i < j and self.isAlpha(s[j]) == False: #garanty to scape non alphnum
                j -= 1
            while i < j and self.isAlpha(s[i]) == False: #garanty to scape non alphnum
                i += 1
            if s[i].lower() != s[j].lower():
                print(s[i])
                print(s[j])
                return False
            else:
                i += 1
                j -= 1

        return True

    def isAlpha(self, ch: str): # function check if the character are alphanumerical
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))

print(Solution().isPalindrome(s))
# print(isApha('z'))
# print(isApha(' '))
# print(isApha(','))


# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         i, j = 0, len(s) - 1

#         while i < j:
#             while i < j and not self.isAlpha(s[i]):
#                 i += 1
#             while i < j and not self.isAlpha(s[j]):
#                 j -= 1

#             if s[i].lower() != s[j].lower():
#                 return False
#             else:
#                 i += 1
#                 j -= 1

#         return True

#     def isAlpha(self, c):
#         return (ord('a') <= ord(c) <= ord('z') or
#                 ord('A') <= ord(c) <= ord('Z') or
#                 ord('0') <= ord(c) <= ord('9'))
