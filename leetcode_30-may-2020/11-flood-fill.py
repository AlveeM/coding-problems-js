from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor: return image
        self.flood_fill_rec(image, sr, sc, newColor, image[sr][sc])
        return image

    def flood_fill_rec(self, image, r, c, newColor, oldColor):
        if (r < 0
            or c < 0
            or r >= len(image)
            or c >= len(image[0])
            or oldColor != image[r][c]): return

        image[r][c] = newColor
        self.flood_fill_rec(image, r+1, c, newColor, oldColor)
        self.flood_fill_rec(image, r-1, c, newColor, oldColor)
        self.flood_fill_rec(image, r, c+1, newColor, oldColor)
        self.flood_fill_rec(image, r, c-1, newColor, oldColor)