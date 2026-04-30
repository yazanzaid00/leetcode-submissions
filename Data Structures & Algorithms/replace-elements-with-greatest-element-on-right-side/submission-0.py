class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        length: int = len(arr)
        for i in range(1,length):
            # slice it and get the maximum
            arr[i-1] = max(arr[i:length:1])

        arr[length-1] = -1
        return arr