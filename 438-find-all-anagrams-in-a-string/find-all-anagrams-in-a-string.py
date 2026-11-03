class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        count=len(p)
        pmap={}
        smap={}
        res=[]
        left=0
        for ch in p:
            pmap[ch]=pmap.get(ch,0)+1

        for right in range(len(s)):
            ch=s[right]
            smap[ch] = smap.get(ch, 0) + 1

            if ch in pmap and smap[ch]<=pmap[ch]:
                count-=1

            if right-left+1>len(p):
                ch=s[left]
               
                if ch in pmap and smap[ch]<=pmap[ch]:
                    count+=1
                smap[ch]-=1
                left+=1
            if count==0:
                res.append(left)

        return res

