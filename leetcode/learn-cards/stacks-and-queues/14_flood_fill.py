class Solution:
    def floodFill(self, image, sr, sc, newColor):
        oldColor = image[sr][sc]
        if oldColor == newColor: return image
        
        m = len(image)
        n = len(image[0])
        
        def floodFillRec(sr, sc):
            if (sr < 0 
                    or sr >= m 
                    or sc < 0 
                    or sc >= n 
                    or image[sr][sc] != oldColor 
                    or image[sr][sc] == newColor):
                return
            
            image[sr][sc] = newColor
            
            floodFillRec(sr+1, sc)
            floodFillRec(sr-1, sc)
            floodFillRec(sr, sc+1)
            floodFillRec(sr, sc-1)
            
        
        floodFillRec(sr, sc)
        return image