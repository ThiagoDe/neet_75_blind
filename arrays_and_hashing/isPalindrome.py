s = "A man, a plan, a canal: Panama"


class Solution:

    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        # print(self.isAlpha(s[j]))
        # print(self.isAlpha(s[i]))
        while i < j:
            while i < j and self.isAlpha(s[j]) == False:
                j -= 1
            while i < j and self.isAlpha(s[i]) == False:
                i += 1
            if s[i].lower() != s[j].lower():
                print(s[i])
                print(s[j])
                return False
            else:
                i += 1
                j -= 1

        return True

    def isAlpha(self, ch: str):
        return (ord('A') <= ord(ch) <= ord('Z') or
                ord('a') <= ord(ch) <= ord('z') or
                ord('0') <= ord(ch) <= ord('9'))

print(Solution().isPalindrome(s))
# print(isApha('z'))
# print(isApha(' '))
# print(isApha(','))
