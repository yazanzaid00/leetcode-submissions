class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length: int = len(arr)
        temp = arr[length-1]
        for i in range(length-1,0,-1):
            test = max(arr[i-1], temp)
            arr[i-1] = temp
            temp = test
        arr[length-1] = -1
        return arr