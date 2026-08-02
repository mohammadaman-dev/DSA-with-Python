"""
Count Even Numbers in an Array

Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def countEven(self, arr):
        count = 0
        for num in arr:
            if num % 2 == 0:
                count += 1
        return count


arr = [12, 13, 14, 15, 16]
answer = Solution().countEven(arr)
print(answer)
