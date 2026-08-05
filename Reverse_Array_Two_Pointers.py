"""
Reverse Array
Topic: Arrays
Approach: Two Pointers
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def reverse(self, arr):
        left = 0
        right = len(arr) - 1
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

arr = [11, 12, 13, 14, 15]
answer = Solution().reverse(arr)
print(answer)
