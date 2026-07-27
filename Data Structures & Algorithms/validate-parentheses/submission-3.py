class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }
        if len(s)%2!=0:
            return False
        for i in s:
            if i in "({[":
                stack.append(i)
            else:
                if not stack or stack[-1] != pairs[i]:
                    return False
                stack.pop()
        return not stack   

        