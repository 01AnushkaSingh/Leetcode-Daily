class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        start=0
        end=0
        if n < 1:
            return ""
        for i in range(n):
            even=self.expand(s,i,i)
            odd=self.expand(s,i,i+1)
            length=max(even,odd)
            if length>end-start:
                start=i-(length-1)//2
                end=i+length//2


        return s[start:end+1]



    def expand(self,s,l,r):
        while(l>=0 and r<len(s) and s[l]==s[r]):
            l-=1
            r+=1

        return r-l-1