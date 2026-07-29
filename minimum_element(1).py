class Solution:
    def minimum(self, arr):
        min_element = arr[0]

        for i in range(1, len(arr)):
            if arr[i] < min_element:
                min_element = arr[i]

        return min_element


arr = [5, 3, 8, 1, 9]
answer = Solution().minimum(arr)
print("Minimum Element:", answer)
