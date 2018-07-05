def n_largest(nums):
    import heapq
    return heapq.nlargest(3,nums)

if __name__ == "__main__":
    nums = [1,2,3,4,3,10,8,22]
    print(n_largest(nums))
