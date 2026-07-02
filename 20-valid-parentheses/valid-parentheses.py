class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["[", "(","{"]
        closing = ["]",")",'}']
        stack = []
        for i in range(len(s)):
            if s[i] in opening:
                stack.append(s[i])
            if s[i] in closing:
                if not stack:
                    return False
                top = stack[-1]
                if (s[i] == ")" and top == "("
                 or s[i] == "]" and top == "["
                  or s[i] == "}" and top == "{"):
                  stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False