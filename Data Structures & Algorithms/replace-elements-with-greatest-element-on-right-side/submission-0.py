class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length= len(arr)
        for i in range (length-1):
            maximum= max(arr[i+1:length])
            arr[i]=maximum
        arr[length-1]=-1
        return arr