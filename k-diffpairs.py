import collections

class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        if k==0:
            return sum(v>1 for v in collections.Counter(nums).values())
        elif k>0:
            return len(set(nums)&set(v+k for v in nums))
        else:
            return 0