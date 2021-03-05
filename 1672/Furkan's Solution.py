class Solution(object):
    def maximumWealth(self, accounts):
        new_list = []
        
        for account in accounts:
            new_list.append(sum(account))
            
        return max(new_list)
