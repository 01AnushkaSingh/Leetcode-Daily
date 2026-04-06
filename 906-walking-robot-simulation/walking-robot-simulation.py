class Solution:
  def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
    DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
    ans = 0
    d = 0 
    x = 0  
    y = 0 
    obstaclesSet = {(x, y) for x, y in obstacles}

    for command in commands:
      if command == -1:
        d = (d + 1) % 4
      elif command == -2:
        d = (d + 3) % 4
      else:
        for _ in range(command):
          if (x + DIRS[d][0], y + DIRS[d][1]) in obstaclesSet:
            break
          x += DIRS[d][0]
          y += DIRS[d][1]
      ans = max(ans, x * x + y * y)

    return ans