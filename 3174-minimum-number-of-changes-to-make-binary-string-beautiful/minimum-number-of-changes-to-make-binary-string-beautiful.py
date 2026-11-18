class Solution:
    def minChanges(self, s: str) -> int:
        change=0
        for i in range(0,len(s),2):
            if s[i] != s[i+1]:
                change+=1
        return change