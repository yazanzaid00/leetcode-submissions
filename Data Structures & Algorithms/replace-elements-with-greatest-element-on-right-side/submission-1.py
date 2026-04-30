class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length: int = len(arr)
        temp = arr[length-1]
        ans = [0]*length
        for i in range(length-1,0,-1):
            temp = ans[i-1] = max(arr[i], temp)
        ans[length-1] = -1
        return ans