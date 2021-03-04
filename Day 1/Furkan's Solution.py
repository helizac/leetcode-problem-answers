class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        
        length_of_list = len(nums)
        length_of_half_list = length_of_list/2
        
        result = []
        
        a = 0
        while a < length_of_half_list:
            result.append(nums[a])
            result.append(nums[a+length_of_half_list])
            a += 1
            
        return result
