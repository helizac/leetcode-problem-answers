class Solution(object):
    def shuffle(self, nums, n):
      
        result = []
        a = 0
        
        while a < n:
            result.append(nums[a])
            result.append(nums[a+n])
            a += 1
            
        return result
