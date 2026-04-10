import collections



class Solution(object):
    def minimumDistance(self, nums):
       
        INF = float("inf")
        result = INF
        lookup = collections.defaultdict(list)
        for i, x in enumerate(nums):
            lookup[x].append(i)
            if len(lookup[x]) < 3:
                continue
            result = min(result, 2*(i-lookup[x][-3]))  
        return result if result != INF else -1
