class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
            closest_x = max(x1, min(x2, xCenter))
            closest_y = max(y1, min(y2, yCenter))

            dist_x = xCenter - closest_x
            dist_y = yCenter - closest_y
            dist_sq = dist_x**2 + dist_y**2

            return dist_sq <= radius**2