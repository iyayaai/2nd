# -*- coding: utf-8 -*-
import re,os,time
# from idlelib.TreeWidget import TreeNode
# from collections import OrderedDict
# from itertools import izip, repeat

'''
Created on 20170701
'''

prices = [0]
print max(prices)
imaxP = prices.index(max(prices))
print imaxP
maxLeft = prices[:imaxP]
print maxLeft


# file1 = 'prices_20171211'
# f = open(file1, 'r')
# contents = f.read()
# f.close()
# list1 = contents.split(',')
# # print len(list1)
# print list1




# prices = [7, 6, 4, 3, 1]
# # prices = [3,2,6,5,0,3]
#  
# maxLeft = prices[:0]
# print maxLeft




# print prices.pop(0)
# print prices









# # Maximum Subarray
# # Status: Accepted, Runtime: 635 ms
# # ----------------------------------------
# class Solution(object):
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
#     def get3SumMaxList(self, nums):     #here nums: PNPN... (after getPosNegList)
#         while True:
#             nums2 = []
#             #print 'nums:',nums
#             len_nums = len(nums)
#             #print 'len_nums:',len_nums
#              
#             while True:
#                 try:
#                     if nums[0] < 0:                     # here: nums should be PNPN...
#                         nums2.append(nums.pop(0))
#                     else:
#                         sum1 = nums[0]+nums[1]+nums[2]
#                         if sum1 >= max([nums[0],nums[1],nums[2]]):
#                             nums2.append(sum1)
#                             nums.pop(0)
#                             nums.pop(0)
#                             nums.pop(0)
#                         else:
#                             nums2.append(nums.pop(0))
#                             nums2.append(nums.pop(0))
#             #                 nums2.append(nums.pop(0))        # xx
#                  
#                 except IndexError:
#                     if len(nums) == 2:
#                         nums2.append(nums.pop(0))
#                         nums2.append(nums.pop(0))
#                         break
#                     if len(nums) == 1:
#                         nums2.append(nums.pop(0))
#                         break
#                     if len(nums) == 0:
#                         break
#                      
#              
#                  
#              
#             #print 'nums2:',nums2
#             len_nums2 = len(nums2)
#             #print 'len_nums2:',len_nums2        
#             nums = nums2
#             #print len_nums, len_nums2
#             #print
#             if len_nums == len_nums2:
#                 return nums2   
#  
#  
#  
#     def isAllNeg(self, nums):
#         for i in nums:
#             if i>0:
#                 return False
#         return True
#  
#  
# 
#     def maxSubArray(self, nums):
#         if self.isAllNeg(nums):
#             return max(nums)
#          
#         nums = self.getPNList(nums)
#         nums = self.get3SumMaxList(nums)
#         maxDigit = max(nums)
#         #print 'maxDigit:', maxDigit
#         pmax = nums.index(maxDigit, )
#         
#         # include pmax:
#         numsLeft = nums[:pmax+1]
#         max0 = 0
#         for i in range(len(numsLeft)):
#             max1 = sum(numsLeft[i:])
#             if max1 >= max0:
#                 max0 = max1
#           
#         #print 'left max:', max0
#         maxLeftSum = max0
#           
#         numsRight = nums[pmax:]
#         max0 = 0
#         for i in range(len(numsRight)):
#             max1 = sum(numsRight[:i+1])
#             if max1 >= max0:
#                 max0 = max1
#                   
#         #print 'right max:', max0
#         maxRightSum = max0
#           
#         maxFinal = maxLeftSum + maxRightSum - maxDigit
#         result = maxFinal  
#         
#         # exclude pmax:
#         numsL = nums[:pmax]
#         try:
#             resL = self.maxSubArray(numsL)
#         except ValueError:
#             resL = result
#         
#         try:
#             numsR = nums[pmax+1:]
#             resR = self.maxSubArray(numsR)
#         except ValueError:
#             resR = result
#         
#         return max(result, resL, resR)







# class Solution(object):
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
#     def get3SumMaxList(self, nums):     #here nums: PNPN... (after getPosNegList)
#         while True:
#             nums2 = []
#             print 'nums:',nums
#             len_nums = len(nums)
#             print 'len_nums:',len_nums
#             
#             while True:
#                 try:
#                     if nums[0] < 0:                     # here: nums should be PNPN...
#                         nums2.append(nums.pop(0))
#                     else:
#                         sum1 = nums[0]+nums[1]+nums[2]
#                         if sum1 >= max([nums[0],nums[1],nums[2]]):
#                             nums2.append(sum1)
#                             nums.pop(0)
#                             nums.pop(0)
#                             nums.pop(0)
#                         else:
#                             nums2.append(nums.pop(0))
#                             nums2.append(nums.pop(0))
#             #                 nums2.append(nums.pop(0))        # xx
#                 
#                 except IndexError:
#                     if len(nums) == 2:
#                         nums2.append(nums.pop(0))
#                         nums2.append(nums.pop(0))
#                         break
#                     if len(nums) == 1:
#                         nums2.append(nums.pop(0))
#                         break
#                     if len(nums) == 0:
#                         break
#                     
#             
#                 
#             
#             print 'nums2:',nums2
#             len_nums2 = len(nums2)
#             print 'len_nums2:',len_nums2        
#             nums = nums2
#             print len_nums, len_nums2
#             print
#             if len_nums == len_nums2:
#                 return nums2   
# 
# 
# 
#     def isAllNeg(self, nums):
#         for i in nums:
#             if i>0:
#                 return False
#         return True
# 
# 
#     
#     
# 
#     def maxSubArray(self, nums):
#         if self.isAllNeg(nums):
#             return max(nums)
#         
#         nums2 = self.getPNList(nums)
#         nums3 = self.get3SumMaxList(nums2)
#         max1 = max(nums3)
#         
#         i_max1 = nums3.index(max1, )
#         numsLeft = []
#         listL = nums3[:i_max1]
#         while True:
#             if listL == []:
#                 break    
#             numsLeft.append(listL.pop())
#         numsRight = nums3[i_max1+1:]
#         
#         listPos = []
#         sumPos = 0
#         for i in numsRight:
#             sumPos = sumPos + i
#             if sumPos>0:
#                 listPos.append(sumPos)
#         
#         sumPos = 0
#         for i in numsLeft:
#             sumPos = sumPos + i
#             if sumPos>0:
#                 listPos.append(sumPos)        
# 
#         if listPos != []:
#             max2 = max(listPos)       
#         else:
#             max2 = 0
#         
#         return max1+max2
#         
#         
# 
# 
# # nums = [-2,1,-3,4,-1,2,1,-5,4]
# # nums = [-2,1,-3,4,-1,3,-5,4]
# # nums = [-39,-58,-44,-95,-68,-47,79,56,52,59,23,64,75,-49,50,61,57,-94,-5,98,95,81,-70,-68,-40,87,-68,-95,30,45,96,90,86,-71,94,94,-19,50,27,-90,9,-50,51,-39,-23,-22,-78,-66,-17,-7,-68,-22,-26,-62,-13,34,-75,18,38,54,-36,11,22,-73,39,-7,98,96,-56,25,83,52,75,34,-86]
# 
# # PNPN..
# # nums = [-2, 1, -3, 6, -5, 4]
# # nums = [-351, 408, -49, 168, -99, 274, -178, 87, -163, 347, -71, 188, -19, 77, -90, 9, -50, 51, -443, 34, -75, 110, -36, 33, -73, 39, -7, 194, -56, 269, -86]
# # nums = [408, -49, 168, -99, 274, -178, 87, -163, 347, -71, 188, -19, 77, -90, 9, -50, 51, -443, 34, -75, 110, -36, 33, -73, 39, -7, 194, -56, 269, -86]
# 
# # nums = [1,-2]
# # nums = [1]
# # nums = [-1]
# # nums = [-1,-2,5]
# 
# # nums = [-1,-2]
# # nums = [-1,-2,0]
# # nums = [-1,-2,-3]
# 
# # nums = [-5,8,-5,1,1,-3,5,5,-3,-3,6,4,-7,-4,-8,0,-1,-6]      # max is 16, not 14 !!
# # nums = [8,-5,1,1,-3,5,5,-3,-3,6,4]
# 
# # nums = [-5,8,-5,1,1,-3,5,5,-3,-3,6,4,-7,-4,-8,0,-1,-6]
# # nums = [-5, 8, -5, 2, -3, 14, -26]
# 
# # nums = [6,-7,-4,4,5,9,7,2,0,-8,1,-5,9,7]        # max should be 31, not 27
# # nums = [6, -11, 27, -8, 1, -5, 16]              # max should be 31, not 27
# 
# # f = open('D:\workspace\Py27_0312\src\DataAnalysis\maxinum subarray_leetcode.txt', 'r')
# # nums = f.read()
# # f.close()
# # nums = nums.split(',')
# # nums = [int(i) for i in nums]       # should be 3452, not 3047
# # 
# # so = Solution()
# # print so.maxSubArray(nums)
# 
# 
# 
# 
# # nums = [6,-7,-4,4,5,9,7,2,0,-8,1,-5,9,7]        # max should be 31, not 27
# # nums = [6, -11, 27, -8, 1, -5, 16]              # max should be 31, not 27
# # nums = [6, -11, 27, -8, 1, -5, 16, 27]
# 
# nums = [-64, 385, -88, 36, -39, 55, -101, 35, -51, 136, -169, 82, -234, 39, -127, 163, -185, 86, -72, 44, -88, 94, -130, 45, -157, 40, -58, 131, -79, 9, -88, 40, -84, 186, -115, 66, -114, 169, -98, 53, -66, 192, -18, 6, -83, 314, -349, 63, -97, 308, -135, 42, -80, 52, -43, 6, -83, 83, -123, 49, -50, 63, -72, 1026, -89, 83, -88, 431, -118, 37, -73, 83, -164, 238, -73, 43, -180, 199, -81, 25, -72, 96, -387, 317, -184, 90, -101, 160, -92, 14, -73, 22, -79, 105, -279, 419, -233, 127, -48, 36, -47, 15, -217, 91, -85, 33, -85, 381, -55, 36, -97, 238, -96, 72, -105, 20, -88, 61, -90, 195, -123, 40, -35, 12, -28, 90, -91, 521, -59, 41, -82, 274, -83, 8, -96, 24, -204, 136, -257, 10, -84, 205, -282, 227, -149, 81, -108, 20, -99, 528, -63, 16, -54, 57, -106, 553, -139, 70, -84, 302, -312, 124, -104, 28, -98, 63, -50, 39, -127, 28, -98, 251, -96, 48, -163, 11, -31, 1105, -113, 28, -32, 179, -80, 10, -54, 467, -96, 31, -232, 283, -119, 14, -93, 61, -136, 75, -75, 59, -304, 30, -56, 172, -150, 114, -54, 47, -226, 177, -135, 43, -34, 3, -32, 142, -206, 90, -21, 8, -26, 24, -91, 31, -196, 194, -94, 86, -122, 201, -57, 19, -49, 112, -110, 40, -147, 98, -110, 62, -306, 44, -167, 367, -51, 10, -110, 577, -211, 112, -193, 210, -147, 131, -233, 44, -103, 33, -44, 17, -267, 160, -261, 93, -95, 313, -279, 55, -140, 166, -94, 32, -54, 57, -258, 55, -106, 155, -189, 98, -106, 31, -94, 51, -195, 90, -220, 183, -65, 40, -86, 38, -180, 114, -134, 37, -87, 103, -191, 261, -247, 17, -19, 278, -152, 22, -110, 44, -71, 92]
# 
#  
#  
# so = Solution()
# # print so.maxSubArray(nums)
# nums = so.getPNList(nums)
# nums = so.get3SumMaxList(nums)
# print nums
# max1 = max(nums)
# print 'max1:',max1
# # print nums.index(max1, )
# i_max1 = nums.index(max1, )
# print 'i_max1:', i_max1
# print
#  
# print nums[:i_max1]
# print nums[i_max1+1:]
# numsLeft = []
# listL = nums[:i_max1]
# while True:
#     if listL == []:
#         break    
#     numsLeft.append(listL.pop())
# print numsLeft
# numsRight = nums[i_max1+1:]
# print numsRight
# print
#  
# listPos = []
# sumPos = 0
# for i in numsRight:
#     sumPos = sumPos + i
#     print sumPos,
#     if sumPos>0:
#         listPos.append(sumPos)
#  
# sumPos = 0
# for i in numsLeft:
#     sumPos = sumPos + i
#     print sumPos,
#     if sumPos>0:
#         listPos.append(sumPos)        
# print
# print 'listPos:', listPos       
# max2 = max(listPos)
# print 'max2:',max2
# print max1+max2




# i1 = nums.index(27, 3)  # L.index(value, [start, [stop]]) -> integer -- return first index of value.
# print i1



# so = Solution()
# # print so.maxSubArray(nums)
# nums = so.getPNList(nums)
# print nums
# nums = so.get3SumMaxList(nums)
# print nums
# 
# if nums[0]<0:
#     nums.pop(0)
# print nums
# if nums[-1]<0:
#     nums.pop(-1)
# print nums





# at office
# class Solution(object):
# #     def getPosNegList(self, nums, i=0, list2=[]):
# #         if i >= len(nums):
# #             return list2            # will get final list2, actually here is the final return!
# #          
# #         sum1 = nums[i]
# #         while True:
# #             if i+1 >= len(nums):
# #                 i = i+1
# #                 break
# #             
# #             if sum1*nums[i+1] >= 0:
# #                 sum1 = sum1 + nums[i+1]
# #                 i = i+1
# #             else:
# #                 i = i+1
# #                 break
# #          
# #         list2.append(sum1)
# #         return self.getPosNegList(nums, i, list2=list2)     # vvv
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
#     def get3SumMaxList(self, nums):     #here nums: PNPN... (after getPosNegList)
#         while True:
#             nums2 = []
#             print 'nums:',nums
#             len_nums = len(nums)
#             print 'len_nums:',len_nums
#             
#             while True:
#                 try:
#                     if nums[0] < 0:                     # here: nums should be PNPN...
#                         nums2.append(nums.pop(0))
#                     else:
#                         sum1 = nums[0]+nums[1]+nums[2]
#                         if sum1 >= max([nums[0],nums[1],nums[2]]):
#                             nums2.append(sum1)
#                             nums.pop(0)
#                             nums.pop(0)
#                             nums.pop(0)
#                         else:
#                             nums2.append(nums.pop(0))
#                             nums2.append(nums.pop(0))
#             #                 nums2.append(nums.pop(0))        # xx
#                 
#                 except IndexError:
#                     if len(nums) == 2:
#                         nums2.append(nums.pop(0))
#                         nums2.append(nums.pop(0))
#                         break
#                     if len(nums) == 1:
#                         nums2.append(nums.pop(0))
#                         break
#                     if len(nums) == 0:
#                         break
#                     
#             
#                 
#             
#             print 'nums2:',nums2
#             len_nums2 = len(nums2)
#             print 'len_nums2:',len_nums2        
#             nums = nums2
#             print len_nums, len_nums2
#             print
#             if len_nums == len_nums2:
#                 return nums2   
# 
# 
# #     def get3SumMaxList(self, nums, i=0, list3 = []):     # here nums: PNPN... (after getPosNegList)
# #         if len(nums) == 1:
# #             list3.append(nums[0])
# #             return list3
# #         
# #         if i+2 == len(nums):
# #             list3.append(nums[i])
# #             list3.append(nums[i+1])
# #             return list3
# #         
# #         if len(nums) < 3:
# #             return
# #         
# #         if i+1 == len(nums):
# #             list3.append(nums[i])
# #             return list3
# #         
# #         try:
# #             if nums[i] >= 0:
# #                 sum3 = nums[i] + nums[i+1] + nums[i+2]
# #                 if sum3 >= max([nums[i],nums[i+1],nums[i+2]]):
# #                     list3.append(sum3)
# #                     i = i+3
# #                 else:
# #                     list3.append(nums[i])
# #                     list3.append(nums[i+1])
# #                     i = i+2
# #             else:
# #                 list3.append(nums[i])
# #                 i = i+1
# #         except IndexError:
# #             return list3
# #         
# #         return self.get3SumMaxList(nums=nums, i=i, list3=list3)
# 
#     def isAllNeg(self, nums):
#         for i in nums:
#             if i>0:
#                 return False
#         return True
# 
#     def maxSubArray(self, nums):
#         if self.isAllNeg(nums):
#             return max(nums)
#         
#         nums2 = self.getPNList(nums)
#         nums3 = self.get3SumMaxList(nums2)
#         nums4 = max(nums3)
#         return nums4
# 
#             
# #     def maxSubArray(self, nums):
# #         while True:
# #             len1 = len(nums)
# # #             nums2 = self.getPosNegList(nums, i=0, list2=[])
# #             nums2 = self.getPNList(nums)
# #             nums = self.get3SumMaxList(nums2, i=0, list3=[])
# #             len2 = len(nums)
# #             if len1 == len2:
# #                 break
# #         return max(nums)  
# 
# 
# # nums = [-2,1,-3,4,-1,2,1,-5,4]
# # nums = [-2,1,-3,4,-1,3,-5,4]
# # nums = [-39,-58,-44,-95,-68,-47,79,56,52,59,23,64,75,-49,50,61,57,-94,-5,98,95,81,-70,-68,-40,87,-68,-95,30,45,96,90,86,-71,94,94,-19,50,27,-90,9,-50,51,-39,-23,-22,-78,-66,-17,-7,-68,-22,-26,-62,-13,34,-75,18,38,54,-36,11,22,-73,39,-7,98,96,-56,25,83,52,75,34,-86]
# 
# # PNPN..
# # nums = [-2, 1, -3, 6, -5, 4]
# # nums = [-351, 408, -49, 168, -99, 274, -178, 87, -163, 347, -71, 188, -19, 77, -90, 9, -50, 51, -443, 34, -75, 110, -36, 33, -73, 39, -7, 194, -56, 269, -86]
# # nums = [408, -49, 168, -99, 274, -178, 87, -163, 347, -71, 188, -19, 77, -90, 9, -50, 51, -443, 34, -75, 110, -36, 33, -73, 39, -7, 194, -56, 269, -86]
# 
# # nums = [1,-2]
# # nums = [1]
# # nums = [-1]
# # nums = [-1,-2,5]
# 
# # nums = [-1,-2]
# # nums = [-1,-2,0]
# # nums = [-1,-2,-3]
# 
# # nums = [-5,8,-5,1,1,-3,5,5,-3,-3,6,4,-7,-4,-8,0,-1,-6]      # max is 16, not 14 !!
# nums = [8,-5,1,1,-3,5,5,-3,-3,6,4]
# 
# so = Solution()
# print so.maxSubArray(nums)

# f = open('D:\workspace\Py27_0312\src\DataAnalysis\maxinum subarray_leetcode.txt', 'r')
# nums = f.read()
# f.close()
# nums = nums.split(',')
# nums = [int(i) for i in nums]

        

# so = Solution()
# print so.getPNList(nums)
# print so.maxSubArray(nums)




# # print so.getPNList(nums)
# nums = so.getPNList(nums)
# nums2 = so.get3SumMaxList(nums)
# print max(nums2)

# print so.maxSubArray(nums)



# # ok
# while True:
#     nums2 = []
#     print 'nums:',nums
#     len_nums = len(nums)
#     print 'len_nums:',len_nums
#     
#     while True:
#         try:
#             if nums[0] < 0:                     # here: nums should be PNPN...
#                 nums2.append(nums.pop(0))
#             else:
#                 sum1 = nums[0]+nums[1]+nums[2]
#                 if sum1 >= max([nums[0],nums[1],nums[2]]):
#                     nums2.append(sum1)
#                     nums.pop(0)
#                     nums.pop(0)
#                     nums.pop(0)
#                 else:
#                     nums2.append(nums.pop(0))
#                     nums2.append(nums.pop(0))
#     #                 nums2.append(nums.pop(0))        # xx
#         
#         except IndexError:
#             if len(nums) == 2:
#                 nums2.append(nums.pop(0))
#                 nums2.append(nums.pop(0))
#                 break
#             if len(nums) == 1:
#                 nums2.append(nums.pop(0))
#                 break
#             if len(nums) == 0:
#                 break
#             
#     
#         
#     
#     print 'nums2:',nums2
#     len_nums2 = len(nums2)
#     print 'len_nums2:',len_nums2        
#     nums = nums2
#     print len_nums, len_nums2
#     print
#     if len_nums == len_nums2:
#         break


# f = open('D:\workspace\Py27_0312\src\DataAnalysis\maxinum subarray_leetcode.txt', 'r')
# nums = f.read()
# f.close()
# nums = nums.split(',')
# nums = [int(i) for i in nums]
# 
# so = Solution()
# nums = so.getPNList(nums)
# print nums
# # print so.get3SumMaxList(nums)
# # print so.maxSubArray(nums)




# # getPNList
# while True:                    # ok
#     len_nums = len(nums)
#     print 'len_nums:', len_nums
#     nums2 = []
#     while True:
#         try:
#             if nums[0]*nums[1] >= 0:
#                 sum1 = nums.pop(0) + nums.pop(0)
#                 nums2.append(sum1)
#             else:
#                 nums2.append(nums.pop(0))
#         except IndexError:
#             print 'nums:', nums
#             if len(nums) == 1:
#                 nums2.append(nums.pop(0))
#             break
#          
#     len_nums2 = len(nums2)
#     print 'nums:', nums
#     print 'nums2:', nums2
#     print 'len_nums2:', len_nums2
#     print
#     if len_nums == len_nums2:
#         break
#     nums = nums2







# so = Solution()
# print so.maxSubArray(nums)
# print so.getPosNegList(nums)    # RuntimeError: maximum recursion depth exceeded

# i = 0
# while True:
#     if nums[i]*nums[i+1] >= 0:
#         sum1 = nums[i] + nums[i+1] 







# class Solution(object):
#     def getMaxNum(self, nums):
#         return max(nums)
#     
#     
#     def getPosNegList(self, nums, i=0, listPN=[]):
# #         if i+2 == len(nums):
# #             return listPN
#         if i+1 == len(nums):
#             return listPN
#         
#         while True:
#             if i == 0:
#                 sum1 = nums[i]
#             try:
#                 if nums[i]*nums[i+1] >= 0:
#                     sum1 = sum1 + nums[i+1]
#                     i = i+1
#                 else:
#                     break
#             except IndexError:
#                 break    
#             
#         print sum1, i
#         listPN.append(sum1)
#         
#         return self.getPosNegList(nums, i+1, listPN)
# 
# 
#     def maxSubArray(self, nums):
#         pass
# 
# # ------------
# # nums = [-2,1,-3,4,-1,2,1,-5,4]
# # nums = [-8]
# # nums = [0]
# # nums = [1,-2]
# # nums = [1,2]
# # nums = [-2,-1,-3,4,-1,2,1,-5,4]
# # nums = [1,2,3,-1]
# nums = [1,2,3,-1,-2]
# 
# so = Solution()
# print 'nums:', nums
# print 'getMaxNum:', so.getMaxNum(nums)
# print 'getPosNegList:', so.getPosNegList(nums)




# dict1 = {
#          '(':')',
#          '[':']',
#          '{':'}',
#          }
# 
# 
# # s = '['
# # s = '()[]{}'
# # s = '()[[]{}'
# list1 = list(s)
# print list1
# 
# 
# 
# # # print list1.pop(0)
# # print dict1[list1.pop(0)] == list1.pop(0)
# # print list1
# 
# while len(list1)!=0:
# #     print dict1[list1.pop(0)] == list1.pop(0)
# #     print list1    
#     if dict1[list1.pop(0)] != list1.pop(0):
#         break
#     else:
#         print list1





# class Solution(object):
#     def isValid(self, s):
#         """
#         :type s: str
#         :rtype: bool
#         """
#         if len(s)<=1:
#             return False
#         
#         dict1 = {
#          '(':')',
#          '[':']',
#          '{':'}',
#          }
#         list1 = list(s)
#         print list1
#         
#         
#         while len(list1)!=0:
#             try:
#                 if dict1[list1.pop(0)] != list1.pop(0):
#                     print list1
#                     #break
#                     return False
#             except KeyError as e:
#                 return False
# 
#         
#         
#         if len(list1) == 0:
#             return True
#         else:
#             return False
# 
# 
# if __name__=='__main__':
# #     s = '['
# #     s = '){'
# #     s = "[])"
# #     s = "(("
#     s = "([])"
#     
#     ss = Solution()
#     print ss.isValid(s)







# class Solution(object):                # time exceed
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
# #         height = [2,5,4,6,7,9,11,8,12,16,13]
#         lenheight = len(height)
#         
#         areaList = []
#         for i in range(lenheight):
#             h1 = height[i]
# #             print height[i],
#             for j in range(i+1, lenheight):
#                 h2 = height[j]
#                 area = (j-i)*min([h1,h2])
#                 areaList.append(area)
# #                 print height[j],
# #                 print '(area=%d)' %(area),
# #             print
# #         print 'maxArea:', max(areaList)       
#         return max(areaList)




# # 11  Container With Most Water   
# # -------------------------------
# class Solution(object):                # # ok
#     def maxArea(self, height):
#         lenheight = len(height)
#         
#         l=0
#         r=lenheight-1
#         
#         max0 = min([height[l], height[r]])*(r-l)
#         print 'max0:', max0
#         while l<r:
#             h1 = height[l]
#             h2 = height[r]
#             max1 = min([h1,h2])*(r-l)
#             if max1>max0:
#                 max0 = max1
#             
#             if h1<=h2:
#                 l+=1
#             else:
#                 r-=1
#         return max0
#         
# #         for i in range(lenheight):
# #             h1 = height[i]
# #             for j in range(i+1, lenheight):
# #                 h2 = height[j]
# #                 area = (j-i)*min([h1,h2])
# #                 areaList.append(area)
# #         return max(areaList)
# 
# 
# if __name__=='__main__':
#     s = Solution()
#     height = [2,5,4,6,7,9,11,8,12,16,13]
#     maxArea = s.maxArea(height)
#     print maxArea








# # list1 = [2,5,4]
# list1 = [2,5,4,6,7,9,11,8,12,16,13]
# lenList1 = len(list1)
# 
# areaList = []
# for i in range(lenList1):
#     h1 = list1[i]
#     print list1[i],
#     for j in range(i+1, lenList1):
#         h2 = list1[j]
#         area = (j-i)*min([h1,h2])
#         areaList.append(area)
#         print list1[j],
#         print '(area=%d)' %(area),
#     print
#         
# print 'maxArea:', max(areaList)






# chain table, from csdn blog
# ------------------------
# class Node(object):
#     def __init__(self, data, pnext = None):
#         self.data = data
#         self._next = pnext
# 
#     def __repr__(self):
#         return str(self.data)
# 
# 
# class ChainTable(object):
#     def __init__(self):
#         self.head = None
#         self.length = 0
# 
#     def isEmpty(self):
#         return (self.length == 0)
# 
#     def append(self, dataOrNode):
#         item = None
#         if isinstance(dataOrNode, Node):
#             item = dataOrNode
#         else:
#             item = Node(dataOrNode)
# 
#         if not self.head:
#             self.head = item
#             self.length += 1
# 
#         else:
#             node = self.head
#             while node._next:
#                 node = node._next
#             node._next = item
#             self.length += 1
# 
#     def delete(self, index):
#         if self.isEmpty():
#             print "this chain table is empty."
#             return
# 
#         if index < 0 or index >= self.length:
#             print 'error: out of index'
#             return
# 
#         if index == 0:
#             self.head = self.head._next
#             self.length -= 1
#             return
# 
#         j = 0
#         node = self.head
#         prev = self.head
#         while node._next and j < index:
#             prev = node
#             node = node._next
#             j += 1
# 
#         if j == index:
#             prev._next = node._next
#             self.length -= 1
# 
#     def insert(self, index, dataOrNode):
#         if self.isEmpty():
#             print "this chain tabale is empty"
#             return
# 
#         if index < 0 or index >= self.length:
#             print "error: out of index"
#             return
# 
#         item = None
#         if isinstance(dataOrNode, Node):
#             item = dataOrNode
#         else:
#             item = Node(dataOrNode)
# 
#         if index == 0:
#             item._next = self.head
#             self.head = item
#             self.length += 1
#             return
# 
#         j = 0
#         node = self.head
#         prev = self.head
#         while node._next and j < index:
#             prev = node
#             node = node._next
#             j += 1
# 
#         if j == index:
#             item._next = node
#             prev._next = item
#             self.length += 1
# 
#     def update(self, index, data):
#         if self.isEmpty() or index < 0 or index >= self.length:
#             print 'error: out of index'
#             return
#         j = 0
#         node = self.head
#         while node._next and j < index:
#             node = node._next
#             j += 1
# 
#         if j == index:
#             node.data = data
# 
#     def getItem(self, index):
#         if self.isEmpty() or index < 0 or index >= self.length:
#             print "error: out of index"
#             return
#         j = 0
#         node = self.head
#         while node._next and j < index:
#             node = node._next
#             j += 1
# 
#         return node.data
# 
# 
#     def getIndex(self, data):
#         j = 0
#         if self.isEmpty():
#             print "this chain table is empty"
#             return
#         node = self.head
#         while node:
#             if node.data == data:
#                 return j
#             node = node._next
#             j += 1
# 
#         if j == self.length:
#             print "%s not found" % str(data)
#             return
# 
#     def clear(self):
#         self.head = None
#         self.length = 0
# 
#     def __repr__(self):
#         if self.isEmpty():
#             return "empty chain table"
#         node = self.head
#         nlist = ''
#         while node:
#             nlist += str(node.data) + ' '
#             node = node._next
#         return nlist
# 
#     def __getitem__(self, ind):
#         if self.isEmpty() or ind < 0 or ind >= self.length:
#             print "error: out of index"
#             return
#         return self.getItem(ind)
# 
#     def __setitem__(self, ind, val):
#         if self.isEmpty() or ind < 0 or ind >= self.length:
#             print "error: out of index"
#             return
#         self.update(ind, val)
# 
#     def __len__(self):
#         return self.length
# 
# 
# 
# # ch = ChainTable(7)    xx
# # print ch            # TypeError: __init__() takes exactly 1 argument (2 given)
# 
# 
# ch = ChainTable()
# # print ch            # empty chain table
# for i in range(10):
#     ch.append(i)
# # print ch        # 0 1 2 3 4 5 6 7 8 9 
# # print ch.getIndex(5)        # 5
# ch.update(0, 99)
# # print ch            # 99 1 2 3 4 5 6 7 8 9 
# ch.update(0, 10)
# # print ch            # 10 1 2 3 4 5 6 7 8 9 
# # ch.delete(10)       # error: out of index
# ch.delete(0)
# # print ch            # 1 2 3 4 5 6 7 8 9 
# ch.insert(0, 100)
# # print ch            # 100 1 2 3 4 5 6 7 8 9 
# # print ch.getItem(5)     # 5
# # print ch[6]             # 6
# 
# 
# # ch2 = ChainTable(ch)
# # print ch2           # TypeError: __init__() takes exactly 1 argument (2 given)
# 
# # node = Node()   xx
# # print node      # TypeError: __init__() takes at least 2 arguments (1 given)
# 
# # node = Node(3)
# # print node          # 3
# 
# # node = Node([1,3,5])
# # # print node, type(node)              # [1, 3, 5]  <class '__main__.Node'>
# # 
# # ch2 = ChainTable()
# # ch2.append(node)
# # print ch2           # [1, 3, 5] 
# # print ch2[0]        # [1, 3, 5]
# # # print ch2[1]        # error: out of index
# # # ch2.append(node)        # xx can not stop after running
# # # print ch2
# 
# ch2 = ChainTable()
# for i in range(100,120):
#     ch2.append(i)
# print ch2           # 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 








# # 2. Add Two Numbers
# # --------------------------------
# 
# class ListNode(object):
#     def __init__(self, x, next=None):
#         self.val = x
#         self.next = next
# 
# L = ListNode('a', ListNode('b', ListNode('c', ListNode('d'))))
# print L
# print L.val
# print L.next.val
# print L.next.next.val
# print L.next.next.next.val




# class ListNode(object):
#     def __init__(self, x, pnext=None):
#         self.val = x
#         self.next = pnext
# 
# 
# l1 = ListNode(135)
# print l1.val
# print l1.next
# print l1.next



# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 
# idx = ListNode(3)
# n = idx
# n.next = ListNode(4)
# n = n.next
# n.next = ListNode(5)
# n = n.next
# print idx




# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = iter(x)
#      
# l1 = ListNode([7,0,8])
# print l1.val
# print l1.next
# print l1.next


# class ListNode(object):              
#     def __init__(self, x):
#         self.val = x
#         list1 = list(str(x))
#         try:
#             self.next = list1.pop(-1)
#         except IndexError as e:
#             pass
# 
# 
# l1 = ListNode(123)
# # print l1.val
# # list1 = list(str(l1.val))
# # print list1.pop(-1)
# # print list1.pop(-1)       
# # print list1.pop(-1)
# # print list1.pop(-1)
# print l1.next
# print l1.next
# print l1.next



# # Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#     
# l1 = ListNode([7,0,8])
# print l1.val
        
        

# l1 = ListNode(123)              # 123
# print l1.val
# list1 = list(str(l1.val))       # ['1', '2', '3']
# print list1



# l1 = [2,4,3]
# # l2 = [5,6,4]
# d1 = 0
# for n,l in enumerate(l1):
#     d1 = d1 + 10**n*l
# print d1





# def getDigit(l1):
#     d1 = 0
#     for n,l in enumerate(l1):
#         d1 = d1 + 10**n*l
#     return d1
# 
# 
# l1 = [2,4,3]
# l2 = [5,6,4]
# 
# d1 = getDigit(l1)
# d2 = getDigit(l2)
# d3 = d1+d2
# print d3
# 
# s3 = str(d3)
# list3 = list(s3)
# print list3
# list.reverse(list3)
# print list3
# list3 = [int(i) for i in list3]
# print list3


# class Solution(object):
#     def getDigit(self, l1):
#         d1 = 0
#         for n,l in enumerate(l1):
#             d1 = d1 + 10**n*l
#         return d1
#      
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """    
#         d1 = self.getDigit(l1)
#         print d1
#         d2 = self.getDigit(l2)
#         print d2
#         d3 = d1+d2
#         print d3
#          
#         s3 = str(d3)
#         list3 = list(s3)
#         list.reverse(list3)
#         list3 = [int(i) for i in list3]
#         return list3        
# 
# 
# if __name__ == '__main__':
#     l1 = [4,5,6]
#     l2 = [5,6,7,8]
#     s = Solution()
#     res = s.addTwoNumbers(l1, l2)
#     print res


# print 10**1












# # Roman to Integer
# # done
# # -------------------------------------
# class Solution(object):
#     def romanToInt(self, s):
#         dict1 = {
#                  'IV':4, 'IX':9,
#                  'XL':40, 'XC':90,
#                  'CD':400, 'CM':900,
#                  }
#         dict2 = {
#                          'M':1000, 
#                 'D':500, 'C':100,
#                 'L':50, 'X':10,
#                 'V':5, 'I':1      
#                 }   
#         
#         numList = []
#         s2 = s
#         for i in dict1:
#             if i in s:
#                 s2 = s2.replace(i, '')
#                 numList.append(dict1[i])
#         
#         for i in list(s2):
#             if i in dict2:
#                 numList.append(dict2[i])
#         
#         return sum(numList)
# 
# if __name__ == '__main__':
#     s = 'MDCCCLXXXVIII'
#     so = Solution()
#     print so.romanToInt(s)





# # Longest Substring Without Repeating Characters
# # done
# # -----------------------------------------------------
# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         list1 = list(s)
#         strDict = {}
#         for i in list1:
#             strDict[i] = 0          # initialize
#         for i in list1:
#             strDict[i] += 1
#         maxLenPossible = len(strDict)
#         
#         listSubString = []
#         max1 = 0
#         for i,s1 in enumerate(list1):
#             subString = s1
#             subList = [s1]
#              
#             for j in range(i+1, len(list1)):
#                 s2 = list1[j]
#                 if s2 in subList:
#                     break
#                 else:
#                     subList.append(s2)
#                     subString = subString + s2
#              
#             listSubString.append(subString)
#             max1 = max1 if max1 > len(subString) else len(subString)
#             if max1 == maxLenPossible:
#                 return max1
#         return max1
# 
# if __name__ == '__main__':
#     #s = 'abcabcbb'
#     #s = 'bbbbb'
#     s = 'pwwkew'
#     #s = ''
#     #s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
#     
#     so = Solution()
#     print so.lengthOfLongestSubstring(s)
        





# class Solution:
#     # @return an integer
#     def lengthOfLongestSubstring(self, s):
#         start = maxLength = 0
#         usedChar = {}
#         
#         for i in range(len(s)):
#             if s[i] in usedChar and start <= usedChar[s[i]]:
#                 start = usedChar[s[i]] + 1
#             else:
#                 maxLength = max(maxLength, i - start + 1)
# 
#             usedChar[s[i]] = i
# 
#         return maxLength
# 
# 
# 
# 
# f = open('string_0702.txt', 'rb')
# s = f.read()                    
# f.close()
# # s = 'abcabcbb'
# # s = 'bbbbb'
# # s = 'b'
# # s = 'bb'
# # s = 'pwwkew'
# # s = ''
# # s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'
# # s = 'abcdefghijklmnoabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'
# # s = 'armstrongirleafuckickofcourse'
# 
# so = Solution()
# print so.lengthOfLongestSubstring(s)



# list1 = list(s)
# # print list1
# # print len(list1)
# 
# def getNoDupString(i, s):
#     #if i+1 < len(list1):
#     if i+1 < len(list(s)):
#         list1 = list(s)
#         subString = list1[i]
#         for j in range(i+1, len(list1)):
#             if list1[j] not in subString:
#                 subString = subString + list1[j]
#             else:
#                 break
# #         print 'subString:', subString
# #         print 'j:', j    
#         return subString, j
#         #return j
#     else:
#         #print 'i+1 >= len(list1)', i+1, len(list1)
#         print 'i+1 >= len(list1)'
#         return len(list(s)) + 10
#     
#     
# def getSubStringList(s):
#     listSubstring = []
#     i = 0
#     while True:
#         subString, i = getNoDupString(i, s)
#         listSubstring.append(subString)
#         if i+1 >= len(list1):
#             break
#     return listSubstring
# 
# 
# listSubstring = getSubStringList(s)
# print listSubstring
# lenListSubstring = [len(i) for i in listSubstring]
# print lenListSubstring

# sub1 = listSubstring[0]         # 1st, [0] add up to [1]
# sub2 = listSubstring[1]
# for i in range(len(sub1)):
#     if sub1[-1] not in sub2:
#         sub2 = sub1[-1] + sub2
#         sub1 = sub1[:-1]
#         print sub1, sub2
# # listSubstring = [sub1, sub2] + listSubstring[2:]
# listSubstring = [sub2] + listSubstring[2:]
# print listSubstring
# 
# for i in listSubstring:
#     print len(i),
# print
# lenListSubstring = lenListSubstring + [len(i) for i in listSubstring]
# print lenListSubstring
# 
# 
# 
# sub1 = listSubstring[0]     # 2nd
# sub2 = listSubstring[1]
# 
# for i in range(len(sub1)):
#     count = 0
#     if sub1[-1] not in sub2:
#         sub2 = sub1[-1] + sub2
#         sub1 = sub1[:-1]
#         print sub1, sub2
#         count+=1
# 
# if count == 0:
#     count+=1
#     sub2 = sub2[:-count]
#     
# for i in range(len(sub1)):
#     if sub1[-1] not in sub2:
#         sub2 = sub1[-1] + sub2
#         sub1 = sub1[:-1]
#         print sub1, sub2
# listSubstring = [sub2] + listSubstring[2:]
# print listSubstring
# lenListSubstring = lenListSubstring + [len(i) for i in listSubstring]
# print lenListSubstring








# while count==0:
#     count2 = count+1
#     count = 0
#     for i in range(len(sub1)):
#         if sub1[-1] not in sub2[:-count2]:
#             sub2 = sub1[-1] + sub2[:-count2]
#             sub1 = sub1[:-1]
#             print sub1, sub2
#             count+=1
#     count2+=1
#     #print 'count2:',count2
#     if count2 == len(sub2):
#         break
        
        





    
# # print s
# print listSubstring
# for i in listSubstring:
#     print len(i),
# print
# # print max(listSubstring)
# print max([len(i) for i in listSubstring])
# 
# sub1 = listSubstring[0]
# print sub1
# print sub1[1:]
# # sub1 = list(sub1)
# # sub1.pop(0)
# # print sub1






# # i = 15
# i = 66
# # i = getNoDupString(i, s)
# # i = getNoDupString(i, s)
# getNoDupString(i, s)




# i = 0
# subString = list1[i]
# for j in range(i+1, len(list1)):
#     if list1[j] not in subString:
#         subString = subString + list1[j]
#     else:
#         break
# 
# print subString
# print j



# subString = list1[0]
# for i,s1 in enumerate(list1):
#     for j in range(i+1, len(list1)):
#         if subString in list1[j:]:
#             break
#         else:
#             subString = subString + list1[j]
#             break
#     print i, len(subString), subString  


 
# max1 = 0
# stringMax = ''
# for i,s1 in enumerate(list1):
#     subString = s1
#     subList = [s1]
#      
#     for j in range(i+1, len(list1)):
#         s2 = list1[j]
#         if s2 in subList:
#             break
#         else:
#             subList.append(s2)
#             subString = subString + s2
#      
#     max1 = max1 if max1 > len(subString) else len(subString)
#     
#     #stringMax = stringMax if len(stringMax)>len(subString) else subString
#     stringMax = stringMax if len(stringMax)>=len(subString) else subString
#      
#     print i, max1, stringMax
     
 
  
     
     





# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         if s == '':
#             return 0
#         
#         else:
#             list1 = list(s)
#             listSubString = []
#             
#             max1 = 0
#             for i,s1 in enumerate(list1):
#                 subString = s1
#                 subList = [s1]
#                 
#                 for j in range(i+1, len(list1)):
#                 #for j in range(i+max1, len(list1)):
#                     s2 = list1[j]
#                     if s2 in subList:
#                         break
#                     else:
#                         subList.append(s2)
#                         subString = subString + s2
#                 
#                 listSubString.append(subString)
#                 #max1 = len(subString)
#                 max1 = max1 if max1 > len(subString) else len(subString)
#                 stringMax = subString
#                 
#                 print max1
#                 
#             
# #             lenSubStringList = [len(i) for i in listSubString]
# #             max1 = max(lenSubStringList)
# #             print max1
#             return max1
#  
#  
# if __name__ == "__main__":
#     #s = 'abcabcbb'
#     #s = 'bbbbb'
#     #s = 'pwwkew'
#     #s = ''
#     s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&'
#     
# #     f = open('string_0702.txt', 'rb')
# #     s = f.read()                    
# #     f.close()
#     
#     print len(s)    # 31652
#     print s
#     
#     
#     so = Solution()
#     print so.lengthOfLongestSubstring(s)










# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         if s == '':
#             #return ''
#             return 0
#         else:
#             list1 = list(s)
#             listSubString = []
#             for i,s1 in enumerate(list1):
#                 subString = s1
#                 subList = [s1]
#                 for j in range(i+1, len(list1)):
#                     s2 = list1[j]
#                     if s2 in subList:
#                         break
#                     else:
#                         subList.append(s2)
#                         subString = subString + s2
#                 listSubString.append(subString)
#             lenSubStringList = [len(i) for i in listSubString]
#             max1 = max(lenSubStringList)
#             for i,j in zip(listSubString, lenSubStringList):
#                 if j == max1:
#                     #return i
#                     return max1
# 
# 
# if __name__ == "__main__":
#     #s = 'abcabcbb'
#     #s = 'bbbbb'
#     #s = 'pwwkew'
#     s = ''
#     so = Solution()
#     print so.lengthOfLongestSubstring(s)


# # s = 'abcabcbb'
# # s = 'bbbbb'
# s = 'pwwkew'
# 
# list1 = list(s)
# print list1
# listSubString = []
# for i,s1 in enumerate(list1):
#     subString = s1
#     subList = [s1]
#     for j in range(i+1, len(list1)):
#         s2 = list1[j]
#         if s2 in subList:
#             break
#         else:
#             subList.append(s2)
#             subString = subString + s2
#     print subList
#     listSubString.append(subString)
# 
# print listSubString
# # for s1 in listSubString:
# #     print len(s1)
# lenSubStringList = [len(i) for i in listSubString]
# print lenSubStringList
# max1 = max(lenSubStringList)
# for i,j in zip(listSubString, lenSubStringList):
#     if j == max1:
#         print i
#         break




# # s = 'abcabcbb'
# s = 'pwwkew'
# 
# list1 = list(s)
# print list1
# for i,s1 in enumerate(list1):
#     subString = s1
#     subList = [s1]
#     for j in range(i+1, len(list1)):
#         #print list1[j],
#         s2 = list1[j]
#         if s2 not in subList:
#             #print s2
#             subList.append(s2)
#             subString = subString + s2
#     print subList
#     print subString
#     #break

    






# # Contains Duplicate III  
# # done
# # --------------------------------------
# class Solution(object):
#     def isDuplicates(self, nums):
#         nums2 = list(set(nums))
#         if len(nums) == len(nums2):
#             return False
#         else:
#             return True
#     
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         if len(nums) <= 1:
#             return False
#         else:
#             if t == 0:
#                 isDup = self.isDuplicates(nums)
#                 if isDup == False:
#                     return False
#                 else:
#                     return True
#             
#             else:
#                 for i, num1 in enumerate(nums):
#                     #if i+k <= len(nums):
#                     if i+k+1 <= len(nums):
#                         #jEnd = i + k 
#                         jEnd = i + k + 1
#                         #jEnd = i + k + 2
#                     else:
#                         jEnd = len(nums)
#                     for j in range(i+1, jEnd):
#                         num2 = nums[j]
#                         if abs(num1 - num2) <= t:
#                             print num1, num2     
#                             return True   
#                 return False
# 
# if __name__ == "__main__":
#     #nums = [5,6,2,8,11,23,45,3,1,9,7,6,43]
#     #nums = [-1,-1,5,6,2,8,11,23,45,3,1,9,7,6,43]
#     #nums = [-1,-1]
# 
#     f = open('nums_20000','rb')
#     list1 = f.readlines()
#     f.close()
#     nums = [int(i.strip()) for i in list1]    # 20000
# 
# #     nums = [2,1]
#     k = 1       # difference between i and j is at most k
#     t = 1       # difference between nums[i] and nums[j] is at most t
#     
#     so = Solution()
#     print so.containsNearbyAlmostDuplicate(nums, k, t)


# ttttttttttttttt
#     k = 3
#     t = 3
#     k = 1       # difference between i and j is at most k
#     t = 0       # difference between nums[i] and nums[j] is at most t
#     k = 10000
#     t = 0
#     nums2 = sorted(set(nums))
#     nums2 = list(OrderedDict(izip(nums, repeat(None))))
#     nums2.append(2433)
#     nums2 = list(set(nums))
#     f = open('nums_20000', 'w')
#     #f.writelines([str(i) for i in nums])
#     f.writelines([str(i)+'\n' for i in nums])
#     f.close()
#     for i in nums:
#         f.write(str(i))
# nums = [5,6,2,8,11,23,45,3,1,9,7,6,43]
# k = 3       # difference between i and j is at most k
# t = 3       # difference between nums[i] and nums[j] is at most t
# for i, num1 in enumerate(nums):
#     #for j in range(i+1, i+k):
#     #for j in range(i+1, lambda x: i+k if i+k <= len(nums) else len(nums)):
#     
#     if i+k <= len(nums):
#         jEnd = i + k
#     else:
#         jEnd = len(nums)
#     for j in range(i+1, jEnd):
#         num2 = nums[j]
#         if abs(num1 - num2) <= t:
#             print num1, num2








# # 10    Regular Expression Matching   
# # done
# class Solution(object):
#     def isMatch(self, s, p):
#         p1 = re.compile(p, re.S)
#         try:
#             result1 = re.search(p1, s).group(0)
#         except:
#             result1 = re.search(p1, s)
#         if result1 == s:
#             return True
#         else:
#             return False
# 
# 
# if __name__ == "__main__":
#     so = Solution()
# #     s = "ab"
# #     p = ".*"
# 
#     s = "ab"
#     p = ".*c"
#     print so.isMatch(s, p)
# 
# 
# # # s = "aaa"
# # # s = "aba"
# # # s = "bbb"
# # # p = "a*"
# # 
# # # s = 'aab'
# # s = 'aabb'
# # # p = "c*a*b"
# # p = "c*a*b*"
# # 
# # p1 = re.compile(p, re.S)
# # # result1 = re.search(p1, s)
# # # print result1.group(0)
# # result1 = re.search(p1, s).group(0)
# # if result1 == s:
# #     print True
# # else:
# #     print False






# 1. Two Sum
# done
# # -------------------------------
# class Solution(object):
#     def twoSum(self, nums, target):
#         for n,num1 in enumerate(nums):
#             for j in range(n+1, len(nums)):
#                 num2 = nums[j]
#                 if num1+num2==target:
#                     print num1, num2
#                     #print [n,j]
#                     return [n,j]
# 
# 
# 
# 
# # nums = [2,7,11,15]
# nums = [2,7,11,15,33,44,55,66]
# # target = 9
# # target = 22
# target = 100
# 
# s = Solution()
# print s.twoSum(nums, target)








# for n,num1 in enumerate(nums):
#     for j in range(n+1, len(nums)):
#         num2 = nums[j]
#         if num1+num2==target:
#             print num1, num2
#             print [n,j]
#             break
    





