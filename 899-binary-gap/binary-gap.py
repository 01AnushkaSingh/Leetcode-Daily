class Solution:
    def binaryGap(self, n: int) -> int:
        binary_str = bin(n)[2:]  
        last_one_index = -1
        max_distance = 0

        for i, char in enumerate(binary_str):
            if char == '1':
                if last_one_index != -1:
                    current_distance = i - last_one_index
                    max_distance = max(max_distance, current_distance)
                last_one_index = i
                
        return max_distance