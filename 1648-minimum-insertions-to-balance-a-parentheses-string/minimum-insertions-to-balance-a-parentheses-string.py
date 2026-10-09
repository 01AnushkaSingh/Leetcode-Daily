class Solution:
  def minInsertions(self, s: str) -> int:
    neededRight = 0  
    missingLeft = 0   
    missingRight = 0 

    for c in s:
      if c == '(':
        if neededRight % 2 == 1:
          missingRight += 1
          neededRight -= 1
        neededRight += 2
      else: 
        neededRight -= 1
        if neededRight < 0:
          missingLeft += 1
          neededRight += 2

    return neededRight + missingLeft + missingRight