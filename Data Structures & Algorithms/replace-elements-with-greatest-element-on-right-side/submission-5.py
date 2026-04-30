class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_element = max(-1, arr[len(arr) - 1])
        arr[len(arr) - 1] = -1
        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = max_element
            max_element = max(max_element, temp)

        return arr