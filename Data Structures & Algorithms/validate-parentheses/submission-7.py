class Solution:
    def isValid(self, s: str) -> bool:
        valid=[]
        valid=list(s)
        stack=[]
        counts = Counter(valid)
        for i in range(len(valid)):
            if(len(valid)%2!=0 or counts["("]!=counts[")"] or counts["{"]!=counts["}"] or counts["["]!=counts["]"]):
                return False
            elif(valid[i]=="("or valid[i]=="{"or valid[i]=="["):
                stack.append(valid[i])
            elif(len(stack)>0):
                if(valid[i]=="}" and stack[-1]=="{"):
                    stack.pop()
                elif(valid[i]==")" and stack[-1]=="("):
                    stack.pop()
                elif(valid[i]=="]" and stack[-1]=="["):
                    stack.pop()
            else:
                return False
        if(len(stack)==0):
            return True
        else:
            return False
            
