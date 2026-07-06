class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        
        intervals.sort(key=lambda x: (x[0], -x[1]))
        
        remaining_count = 0
        max_end = 0
        
        for _, end in intervals:
          
            if end > max_end:
                remaining_count += 1
                max_end = end
                
        return remaining_count  