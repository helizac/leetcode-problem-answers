#Solution 1 with back tracking algorithm
class Solution1(object):
    def permute(self, nums):
        answer = []
        
        n = len(nums)

        def tracking(cl):
            if len(cl) == n:
                answer.append(cl)
                return
            for i in range(n):
                if nums[i] not in cl:
                    tracking(cl + [nums[i]])
        tracking([])
            
        return answer

#Solution 2 with just using list and basics
class Solution2(object):
    def permute(self, nums):
        
        list = []
        result = []
        last_result = []
        numbers = []
        y = 0
        
        for a in range(1, len(nums)+1):
            length = pow(len(nums),a)
            list.append([])
            x = 0
            while x < length:
                for b in range(len(nums)):
                    list[a-1].append(nums[b])
                x += len(nums)
        
        for i in range(len(nums)):
            numbers.append(0)

        while y < len(list[len(list)-1]):
            result.append([])
            for i in range(0,len(nums)-1):
                if y%int((len(list[len(list)-1])/pow(len(nums),(i+1)))) == 0 and y != 0:
                        numbers[i] += 1
            for i in range(0,len(nums)-1):
                result[y].append(list[i][numbers[i]])
            result[y].append(list[len(nums)-1][y])
            y += 1

        for i in result:
            j = i
            i = []
            for a in j:
                if a not in i:
                    i.append(a)
            if len(i) == len(nums):
                last_result.append(i)
