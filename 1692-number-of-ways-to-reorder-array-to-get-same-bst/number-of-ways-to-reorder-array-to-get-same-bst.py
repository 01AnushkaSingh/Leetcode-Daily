class Solution(object):
    def numOfWays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def count_bst_permutations(arr):
            
            if len(arr) < 2:
                return 1
          
            root = arr[0]
            left_subtree = [x for x in arr if x < root]
            right_subtree = [x for x in arr if x > root]
          
            left_size = len(left_subtree)
            right_size = len(right_subtree)
          
            left_permutations = count_bst_permutations(left_subtree)
            right_permutations = count_bst_permutations(right_subtree)
          

            total_size = left_size + right_size
            combinations = binomial_coefficients[total_size][left_size]
          
            result = (combinations * left_permutations % MOD) * right_permutations % MOD
            return result
      
        n = len(nums)
        MOD = 10**9 + 7

        binomial_coefficients = [[0] * n for _ in range(n)]
        binomial_coefficients[0][0] = 1
      
        for i in range(1, n):
            binomial_coefficients[i][0] = 1  # C(i, 0) = 1
            for j in range(1, i + 1):
                # Pascal's triangle formula: C(i, j) = C(i-1, j) + C(i-1, j-1)
                binomial_coefficients[i][j] = (
                    binomial_coefficients[i - 1][j] + 
                    binomial_coefficients[i - 1][j - 1]
                ) % MOD
      
        total_permutations = count_bst_permutations(nums)
        return (total_permutations - 1 + MOD) % MOD
      