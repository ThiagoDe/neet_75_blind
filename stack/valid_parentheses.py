class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # closeToOpen = {
        #     ']': '[',
        #     '}': '{',
        #     ')': '('
        # }

        # for c in s:
        #     if c not in closeToOpen:
        #         stack.append(c)
        #     else:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
        #         else:
        #             return False

        # return not stack

        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0

s = "()[]{}"
print(Solution().isValid(s))


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return True if not stack else False
