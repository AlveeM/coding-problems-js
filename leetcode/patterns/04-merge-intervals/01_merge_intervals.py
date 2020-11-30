class Solution:
    def merge(self, intervals):
        if len(intervals) <= 1: return intervals
        
        intervals.sort(key=lambda interval: interval[0])
        mergedIntervals = []
        start = intervals[0][0]
        end = intervals[0][1]
        
        for i in range(1, len(intervals)):
            interval = intervals[i]
            
            if interval[0] <= end:
                end = max(end, interval[1])
            else:
                mergedIntervals.append([start, end])
                start = interval[0]
                end = interval[1]
                
        mergedIntervals.append([start, end])
        return mergedIntervals