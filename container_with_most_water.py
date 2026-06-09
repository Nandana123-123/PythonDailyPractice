def maxArea( height):
        max_area=0
        left=0
        right=len(height)-1
        while(left<right):
            width=right-left
            max_water=min(height[left],height[right])
            cur_area=max_water*width
            if cur_area>max_area:
                max_area=cur_area

            if height[left]<height[right]:
                left+=1
            else:
                right-=1

        return max_area

height=[int(x) for x in input("Enter a numbers: ").split()]
print(maxArea(height))