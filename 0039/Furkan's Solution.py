class Solution(object):
    def combinationSum(self, candidates, target):
        
        answer = []
        n = len(candidates)
        
        # cc = current_combination
        # ccs = current_combination_summary
        # ic = i_current
        
        def backtracking(cc, ccs, ic):
            if ccs > target: return
            if ccs == target: answer.append(cc)
            for i in range(ic, n):
                backtracking(cc + [candidates[i]], ccs + candidates[i], i)
            
        backtracking([], 0, 0)
        return answer
