class Solution(object):
    def removeDuplicates(self, nums):
        a = 0
        while a < len(nums)-1:
            if nums.count(nums[a]) > 1:
                nums.remove(nums[a])
                a = a-1
            a += 1
        return len(nums)
