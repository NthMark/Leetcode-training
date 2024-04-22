def maxArea(height: list[int]) -> int:
        area=0
        for i in range(len(height)):
            for j in range(len(height)):
                if height[i]<=height[j]:
                    tempArea=height[i]*abs(i-j)
                    if area<tempArea:
                        area=tempArea
        
        return area
if __name__=='__main__':
     print(maxArea([2,3,5,7,2]))