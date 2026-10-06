class Solution:
    def isValid(self, s: str) -> bool:
        brackets={")":"(","}":"{","]":"["}
        stack=[]
        for c in s:
            if (c in brackets and len(stack)!=0):
                if(brackets[c]==stack[-1]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        else:
            return True
