class Solution:
    def countSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        for i in range(n):
            count+=self.expand(s,i,i)
            count+=self.expand(s,i,i+1)
        return count


    def expand(self,s,l,r):
        count=0
        while (l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1
            count+=1
        return count