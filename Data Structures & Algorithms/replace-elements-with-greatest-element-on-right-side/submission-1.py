class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length= len(arr)
        temp=arr[length-1]
        arr[length-1]=-1
        maximum=-1
        
        for i in range (length-2,-1,-1):
            if(temp>maximum):
                maximum=temp
                temp=arr[i]
                arr[i]=maximum
            else:
                temp=arr[i]
                arr[i]=maximum
        return arr