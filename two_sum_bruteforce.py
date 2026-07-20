"""
LeetCode #1 - Two Sum
Author: Mohammad Aman
Approach: Brute Force
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

class Solution:
    def twoSum(self, arr, target):
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] == target:
                    return (i, j)
        return -1


if __name__ == "__main__":
    arr = [12, 23, 45, 244]
    target = 256

    answer = Solution().twoSum(arr, target)
    print(answer)
