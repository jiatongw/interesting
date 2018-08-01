class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        left = mid = 0
        right = len(nums) - 1
        while mid <= right:
            if nums[mid] == 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


if __name__ == "__main__":
    l = [1, 2, 1, 2, 0, 2, 1, 0, 2, 0, 0, 2]
    Solution().sortColors(l)
    assert l == [0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]