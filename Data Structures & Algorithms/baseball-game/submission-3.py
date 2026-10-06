class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]
        add=0
        for i in range(len(operations)):
            
            if(operations[i]=="+"):
                for i in range(len(record)-1,len(record)-2,-1):
                    add= record[i]+record[i-1]
                record.append(add)
            elif(operations[i]=="C"):
                record.pop()
            elif(operations[i]=="D"):
                record.append(record[len(record)-1]*2)
            else:
                record.append(int(operations[i]))
        return sum(record)
