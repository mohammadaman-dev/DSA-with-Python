class Solution:
    def maximumElement(self, arr):
        maximum = arr[0]
        for i in range(len(arr)):
            if arr[i] > maximum:
                maximum = arr[i]
        return maximum

arr = [12, 45, 23, 67, 34]
answer = Solution().maximumElement(arr)
print(answer)
