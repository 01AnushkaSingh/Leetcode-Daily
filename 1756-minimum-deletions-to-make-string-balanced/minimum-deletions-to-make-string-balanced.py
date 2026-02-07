class Solution(object):
    def minimumDeletions(self, s):
        
        leftb = 0
        righta = s.count('a')
        ans = righta
        for c in s:
            if c == 'a':
                righta -= 1
            else:
                leftb += 1
            ans = min(ans, leftb + righta)
        return ans