class Solution:
    def insert(self, intervals, newInterval):
        res = []
        i = 0
        
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
            
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
            
        res.append(newInterval)
        
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
            
        return res

class Solution2:
    def insert(self, intervals, newInterval):
        if not intervals: return [newInterval]
        
        left = []
        right = []
        new_start = newInterval[0]
        new_end = newInterval[1]
        
        for start, end in intervals:
            if end < new_start:
                left.append([start, end])
            elif start > new_end:
                right.append([start, end])
            else:
                new_start = min(new_start, start)
                new_end = max(new_end, end)
        
        return left + [[new_start, new_end]] + right