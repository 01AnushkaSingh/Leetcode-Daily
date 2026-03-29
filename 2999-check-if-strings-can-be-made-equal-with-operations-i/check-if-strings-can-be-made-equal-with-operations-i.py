class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        
        even1 = sorted(s1[0::2])
        odd1 = sorted(s1[1::2])
        even2 = sorted(s2[0::2])
        odd2 = sorted(s2[1::2])
        
        return even1 == even2 and odd1 == odd2