class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        while len(intervals) >= 1:
            l = len(intervals)
            i = 0
            while i < len(intervals)-1:
                if intervals[i][1] >= intervals[i+1][0]:
                    intervals[i].extend(intervals[i+1])
                    intervals.remove(intervals[i+1])
                    intervals[i].sort()
                    intervals[i] = [intervals[i][0],intervals[i][len(intervals[i])-1]]
                    i -= 1
                i += 1
            if l == len(intervals):
                return intervals
            
        return intervals
