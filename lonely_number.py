class Solution:
    def validIPAddress(self, l):
        for i in l:
            if l.count(i) == 1:
                return i

if __name__ == '__main__':
    s = Solution()
    print(s.validIPAddress([1,1,1,2,3,1,3,5,5]))