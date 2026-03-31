class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        # Initialize the result string as a list of '?' (unknown characters)
        ans = ['?'] * (n + m - 1)
        # Track which positions in the result string are fixed by 'T' constraints
        fixed = [False] * (n + m - 1)

        # First pass: Process all 'T' constraints to fix characters
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    if fixed[i + j] and ans[i + j] != str2[j]:
                        # Contradiction found: impossible to satisfy all 'T' constraints
                        return ""
                    ans[i + j] = str2[j]
                    fixed[i + j] = True

        # Second pass: Check for immediate 'F' constraint violations after 'T' pass
        for i in range(n):
            if str1[i] == 'F':
                # Check if the current substring fully matches str2
                if "".join(ans[i:i + m]) == str2:
                    # If it matches, and all characters in this window were fixed by 'T' constraints,
                    # a contradiction exists. If some are not fixed, we resolve it later.
                    can_change = False
                    for j in range(m):
                        if not fixed[i + j]:
                            can_change = True
                            break
                    if not can_change:
                        return ""

        # Third pass: Greedily fill remaining '?' with 'a' (the lexicographically smallest character)
        for i in range(len(ans)):
            if ans[i] == '?':
                ans[i] = 'a'

        # Fourth pass: Resolve remaining 'F' violations by changing the rightmost unfixed 'a' to 'b'
        for i in range(n):
            if str1[i] == 'F':
                if "".join(ans[i:i + m]) == str2:
                    # Violation found, flip the rightmost non-fixed character in the window to 'b'
                    for j in range(m - 1, -1, -1):
                        if not fixed[i + j]:
                            ans[i + j] = 'b'
                            break
                    # The problem statement guarantees a solution exists if we reach this point (implied by constraints/logic)

        return "".join(ans)
