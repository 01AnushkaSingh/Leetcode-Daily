class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        ROWS, COLS = len(boxGrid), len(boxGrid[0])
        
        
        for r in range(ROWS):
            
            empty_ptr = COLS - 1
            for c in range(COLS - 1, -1, -1):
                if boxGrid[r][c] == "#":
                   
                    boxGrid[r][c], boxGrid[r][empty_ptr] = boxGrid[r][empty_ptr], boxGrid[r][c]
                    empty_ptr -= 1
                elif boxGrid[r][c] == "*":
                   
                    empty_ptr = c - 1
     
        res = [[""] * ROWS for _ in range(COLS)]
        for r in range(ROWS):
            for c in range(COLS):
                res[c][ROWS - 1 - r] = boxGrid[r][c]
                
        return res