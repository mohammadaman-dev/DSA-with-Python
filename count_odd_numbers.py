class Solution:
    def countOdd(self, arr):
        count = 0

        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                count += 1

        return count


arr = [12, 13, 14, 15, 16]
answer = Solution().countOdd(arr)
print(answer)
