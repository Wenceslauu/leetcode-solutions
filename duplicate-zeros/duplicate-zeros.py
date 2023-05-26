class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        length = len(arr)
        count = 0
        
        for i in range(length):
            if arr[i + count] == 0:
                arr.insert(i + count, 0)
                
                count += 1
                
        for i in range(count):
            arr.pop()