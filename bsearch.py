class Solution:
    def bsearch(self, nums, target):
        """Binary search of a target in a sorted array
        without duplicates. If such a target does not exist,
        return -1, othewise, return its index.
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

s = Solution()
a = [1,3,5,6,7,9,11]
print(s.bsearch(a, 7))
