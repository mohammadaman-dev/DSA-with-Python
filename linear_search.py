"""
Linear Search
Author: Mohammad Aman
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def linearSearch(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1


if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    target = 30

    answer = Solution().linearSearch(arr, target)
    print(answer)
