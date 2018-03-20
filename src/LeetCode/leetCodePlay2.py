# -*- coding: utf-8 -*-


def power(x,n):
    if n==1:
        result = 1
        return result
    
    if n%2==0:
        result = power(x,n/2)*power(x,n/2)
    else:
        result = power(x,(n+1)/2)*power(x,(n-1)/2)
    return result
        
x = 5
n = 3
print power(5, 3)


print pow(5, 3)




# class Solution(object):
#     def getPosNegList(self, nums, i=0, list2=[]):
#         if i >= len(nums):
#             return list2            # will get final list2, actually here is the final return!
#            
#         sum1 = nums[i]
#         while True:
#             if i+1 >= len(nums):
#                 i = i+1
#                 break
#               
#             if sum1*nums[i+1] >= 0:
#                 sum1 = sum1 + nums[i+1]
#                 i = i+1
#             else:
#                 i = i+1
#                 break
#            
#         list2.append(sum1)
#         return self.getPosNegList(nums, i, list2=list2)     # vvv
#  
#  
#     def getPNList(self, nums):
#         while True:
#             len_nums = len(nums)
# #             print 'len_nums:', len_nums
#             nums2 = []
#             while True:
#                 try:
#                     if nums[0]*nums[1] >= 0:
#                         sum1 = nums.pop(0) + nums.pop(0)
#                         nums2.append(sum1)
#                     else:
#                         nums2.append(nums.pop(0))
#                 except IndexError:
# #                     print 'nums:', nums
#                     if len(nums) == 1:
#                         nums2.append(nums.pop(0))
#                     break
#                  
#             len_nums2 = len(nums2)
# #             print 'nums:', nums
# #             print 'nums2:', nums2
# #             print 'len_nums2:', len_nums2
# #             print
#             if len_nums == len_nums2:
#                 #break
#                 return nums2
#             nums = nums2
#  
#  
# #     def get3SumMaxList(self, nums):     #here nums: PNPN... (after getPosNegList)
# #         while True:
# #             nums2 = []
# #             print 'nums:',nums
# #             len_nums = len(nums)
# #             print 'len_nums:',len_nums
# #              
# #             while True:
# #                 try:
# #                     if nums[0] < 0:                     # here: nums should be PNPN...
# #                         nums2.append(nums.pop(0))
# #                     else:
# #                         sum1 = nums[0]+nums[1]+nums[2]
# #                         if sum1 >= max([nums[0],nums[1],nums[2]]):
# #                             nums2.append(sum1)
# #                             nums.pop(0)
# #                             nums.pop(0)
# #                             nums.pop(0)
# #                         else:
# #                             nums2.append(nums.pop(0))
# #                             nums2.append(nums.pop(0))
# #             #                 nums2.append(nums.pop(0))        # xx
# #                  
# #                 except IndexError:
# #                     if len(nums) == 2:
# #                         nums2.append(nums.pop(0))
# #                         nums2.append(nums.pop(0))
# #                         break
# #                     if len(nums) == 1:
# #                         nums2.append(nums.pop(0))
# #                         break
# #                     if len(nums) == 0:
# #                         break
# #                      
# #              
# #                  
# #              
# #             print 'nums2:',nums2
# #             len_nums2 = len(nums2)
# #             print 'len_nums2:',len_nums2        
# #             nums = nums2
# #             print len_nums, len_nums2
# #             print
# #             if len_nums == len_nums2:
# #                 return nums2   
#  
#  
#     def get3SumMaxList(self, nums, i=0, list3 = []):     # here nums: PNPN... (after getPosNegList)
#         if len(nums) == 1:
#             list3.append(nums[0])
#             return list3
#          
#         if i+2 == len(nums):
#             list3.append(nums[i])
#             list3.append(nums[i+1])
#             return list3
#          
#         if len(nums) < 3:
#             return
#          
#         if i+1 == len(nums):
#             list3.append(nums[i])
#             return list3
#          
#         try:
#             if nums[i] >= 0:
#                 sum3 = nums[i] + nums[i+1] + nums[i+2]
#                 if sum3 >= max([nums[i],nums[i+1],nums[i+2]]):
#                     list3.append(sum3)
#                     i = i+3
#                 else:
#                     list3.append(nums[i])
#                     list3.append(nums[i+1])
#                     i = i+2
#             else:
#                 list3.append(nums[i])
#                 i = i+1
#         except IndexError:
#             return list3
#          
#         return self.get3SumMaxList(nums=nums, i=i, list3=list3)
#  
#     def isAllNeg(self, nums):
#         for i in nums:
#             if i>0:
#                 return False
#         return True
#  
# #     def maxSubArray(self, nums):
# #         if self.isAllNeg(nums):
# #             return max(nums)
# #          
# #         nums2 = self.getPNList(nums)
# #         nums3 = self.get3SumMaxList(nums2)
# #         nums4 = max(nums3)
# #         return nums4
#  
#              
#     def maxSubArray(self, nums):
#         while True:
#             len1 = len(nums)
#             nums2 = self.getPosNegList(nums, i=0, list2=[])
# #             nums2 = self.getPNList(nums)
#             nums = self.get3SumMaxList(nums2, i=0, list3=[])
#             len2 = len(nums)
#             if len1 == len2:
#                 break
#         return max(nums)  
#     
#     
#     
# f = open('D:\workspace\Py27_0312\src\DataAnalysis\maxinum subarray_leetcode.txt', 'r')
# nums = f.read()
# f.close()
# nums = nums.split(',')
# nums = [int(i) for i in nums]       # should be 3452, not 3047
# 
# so = Solution()
# print so.maxSubArray(nums)    


