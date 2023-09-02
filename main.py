'''
Array Series !!
################################################################################################################################################################################ 11 ####################################################################
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
class Solution:
    def maxArea(self, height: List[int]) -> int:



def maxArea(self, height: List[int]) -> int:
        res = 0
        l = 0
        r = len(height)-1
        while l<r:
            area = (r-l)*min(height[l],height[r])
            res = max(res,area)
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return res


'''


# def maxArea(height):
#     maxI = 0
#     for l in range(len(height)):
#         for r in range(l+1,len(height)):
#             area = (r-l)* min(height[l],height[r])
#             maxI = max(maxI,area)
#     return maxI
#
#
#
#
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# s = maxArea(height)
# print(s)

#############################################################################################################################
####################################### 15 ##################################################################################
# nums = [-1,0,1,2,-1,-4]
#
# trips = []
# for i in range(len(nums)):
#     for j in range(i,len(nums)):
#         for k in range(j,len(nums)):
#             if(i==j==k):
#                 continue
#             else:
#                 if(i!=j and i!=k and j!=k):
#                     if(nums[i]+nums[j]+nums[k] == 0):
#                         ele = [nums[i],nums[j],nums[k]]
#                         ele = sorted(ele)
#                         print(ele)
#                         if ele in trips:
#                             continue
#                         else:
#                             trips.append(ele)
# print(sorted(trips))

# working, but time limit exceeding for extreme test cases..



#optimizing:
nums = [-1,0,1,2,-1,-4]
trips = []
for i in range(len(nums)):
    a = nums[i]
    start,end = i+1 , len(nums)-1
    t = -a
    while(start<end):
        print(start,end)
        if(nums[start]+nums[end] == t):
            print(nums[start],nums[end],a)
            s = [a,nums[start],nums[end]]
            trips.append(s)
        elif(nums[start]+nums[end] > t):
            end-=1
        else:
            start+=1
print(trips)
