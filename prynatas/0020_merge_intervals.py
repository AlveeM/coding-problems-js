class Solution:
    def merge(self, intervals):
        # check if single interval and return input if true
        if len(intervals) <= 1: return intervals
        
        # sort the intervals based on start time
        # JavaScript: intervals.sort((a, b) => a[0] - b[0])
        intervals.sort(key=lambda interval: interval[0])
        # declare a variable to track new intervals
        new_intervals = []
        # declare a variable to store last start time
        last_start = intervals[0][0]
        # declare a variable to store last end time
        last_end = intervals[0][1]
        
        # iterate through intervals starting at the 2nd interval
        for i in range(1, len(intervals)):
            cur_interval = intervals[i]
            # if overlapping; cur_interval[0] -> current interval's start time
            if cur_interval[0] <= last_end:
                last_end = max(last_end, cur_interval[1])
            else:
                new_intervals.append([last_start, last_end])
                last_start = cur_interval[0]
                last_end = cur_interval[1]
        
        # add the last interval to the new intervals
        new_intervals.append([last_start, last_end])
        
        # return new intervals
        return new_intervals