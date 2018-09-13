class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        strs = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        
        res=''
        
        for i in range(0,len(nums)):
            while num - nums[i] >= 0:
                res+=strs[i]
                num = num - nums[i]
                
        return res
