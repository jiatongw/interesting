# def n_largest(nums):
#     import heapq
#     return heapq.nlargest(3,nums)
#
# if __name__ == "__main__":
#     nums = [1,2,3,4,3,10,8,22]
#     print(n_largest(nums))
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import heapq
        min_heap = [-float('inf')]*k
        heapq.heapify(min_heap)
        for num in nums:
            if num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,num)
        return min_heap[0]

if __name__ == "__main__":
    nums = [1,2,3,4,3,10,8,22]
    s=Solution()
    print(s.findKthLargest(nums,3))


