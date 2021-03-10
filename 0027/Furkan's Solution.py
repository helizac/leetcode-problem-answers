class Solution(object):
    def removeElement(self, nums, val):
      
        a = 0
        while a < len(nums)+2:
            for i in range(len(nums)):
                if nums[i] == val:
                    nums.remove(nums[i])
                    break
            a += 1

        return len(nums)
