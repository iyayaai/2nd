# -*- coding: utf-8 -*-



class Solution(object):
#     def get_maxmin(self, prices):
#         if len(prices) == 0:
#             return 0, 0, 0, 0, 0        
#         maxP = max(prices)    
#         minP = min(prices)  
#         imaxP = prices.index(maxP)  
#         iminP = prices.index(minP)   
#         
#         if imaxP == 0:
#             prices.pop(0)
#             return self.get_maxmin(prices)
#         else:
#             return prices, maxP, minP, imaxP, iminP

    def get_maxmin(self, prices):
        if len(prices) == 0:
            return 0, 0, 0, 0, 0      
        
        maxP = max(prices)    
        minP = min(prices)  
#         minP = 0
        imaxP = prices.index(maxP)  
        iminP = prices.index(minP)   
#         iminP =0
        
        while imaxP == 0 and len(prices) > 1:
            prices.pop(0)
            maxP = max(prices)    
            minP = min(prices)  
            imaxP = prices.index(maxP)  
            iminP = prices.index(minP)  
            
        while iminP == len(prices) - 1 and len(prices) > 1:
            prices.pop(-1)
            maxP = max(prices)    
            minP = min(prices)  
            imaxP = prices.index(maxP)  
            iminP = prices.index(minP)              
        
        return prices, maxP, minP, imaxP, iminP
                    

    def handle_maxLeft(self, prices, maxP, imaxP):
        if prices != 0 and len(prices) > 1:
            maxLeft = prices[:imaxP]
            result = maxP - min(maxLeft)
            return result
        else:
            return 0
    
    def handle_maxRight(self, prices, imaxP):
        if prices == 0:
            return 0
        else:
            maxRight = prices[imaxP+1:]
            if maxRight == []:
                prices = 0
            else:
                prices = maxRight
            return prices
         

    def maxProfit(self, prices):
        resultList = []
        while prices != 0:
            prices, maxP, minP, imaxP, iminP = self.get_maxmin(prices)
            result = self.handle_maxLeft(prices, maxP, imaxP)
            resultList.append(result)
            prices = self.handle_maxRight(prices, imaxP)
        return max(resultList)



# prices = [7, 1, 5, 3, 6, 4]             # 5
# prices = [7, 1, 5, 3, 9, 6, 4]           # 8
# prices = [7, 6, 4, 3, 1]            # 0
# prices = [2,4,1]                    # 2
# prices = [3,2,6,5,0,3]            # 4
# prices = [1,2]                      # 1
  
file1 = 'prices_20171211'
f = open(file1, 'r')
contents = f.read()
f.close()
prices = contents.split(',')
prices = [int(i) for i in prices]
  
so = Solution()
print so.get_maxmin(prices)
# print so.maxProfit(prices)






# class Solution(object):
#     def get_maxmin(self, prices):
#         maxP = max(prices)    
#         minP = min(prices)  
#         imaxP = prices.index(maxP)  
#         iminP = prices.index(minP)   
#         return maxP, minP, imaxP, iminP 
# 
# 
#     def removeBorder(self, prices):
#         maxP, minP, imaxP, iminP = self.get_maxmin(prices)
#         lenPrices = len(prices)
#         # border
#         if iminP == lenPrices-1:
#             prices.pop(-1)
#             if len(prices) == 0:
#                 return 0            
#             minP = min(prices)
#         # border
#         if imaxP == 0:
#             prices.pop(0)
#             if len(prices) == 0:
#                 return 0              
#             maxP = max(prices)    
#         return prices
#     
#     
#     def maxProfit(self, prices):
#         if len(prices) == 0:
#             return 0
#   
#          
# #         lenPrices = len(prices)
# #         maxP = max(prices)    
# #         minP = min(prices)  
# #         imaxP = prices.index(maxP)  
# #         iminP = prices.index(minP)
#           
# #         maxLeft = prices[:imaxP]
#          
# #         if maxLeft != []:
# #             result = maxP - min(maxLeft)
# #         else:
# #             pass
# #   
# #   
# #         # border
# #         if iminP == lenPrices-1:
# #             prices.pop(-1)
# #             if len(prices) == 0:
# #                 return 0            
# #             minP = min(prices)
# #           
# #         # border
# #         if imaxP == 0:
# #             prices.pop(0)
# #             if len(prices) == 0:
# #                 return 0              
# #             maxP = max(prices)
# #           
# #         imaxP = prices.index(maxP)  
# #         iminP = prices.index(minP)
# #             
# #         def isMaxBehindMin(imaxP, iminP):
# #             if imaxP > iminP:
# #                 return True
# #             else:
# #                 return False
# #                  
# #         if isMaxBehindMin(imaxP, iminP):
# #             if result > prices[imaxP] - prices[iminP]:
# #                 return result
# #             else:
# #                 result = prices[imaxP] - prices[iminP]
# #                 return result
# #               
# #         else:
# #             prices.pop(imaxP)
# #             return self.maxProfit(prices)      



 















# class Solution(object):
#     def maxProfit(self, prices):
#         if len(prices) == 0:
#             return 0
#  
#         
#         lenPrices = len(prices)
#         maxP = max(prices)    
#         minP = min(prices)  
#         imaxP = prices.index(maxP)  
#         iminP = prices.index(minP)
#          
#         maxLeft = prices[:imaxP]
#         
#         if maxLeft != []:
#             result = maxP - min(maxLeft)
#         else:
#             pass
# #         try:
# #             result = maxP - min(maxLeft)
# #         except ValueError as e:
# #             pass
#  
#  
#         # border
#         if iminP == lenPrices-1:
#             prices.pop(-1)
#             if len(prices) == 0:
#                 return 0            
#             minP = min(prices)
#          
#         # border
#         if imaxP == 0:
#             prices.pop(0)
#             if len(prices) == 0:
#                 return 0              
#             maxP = max(prices)
#          
#         imaxP = prices.index(maxP)  
#         iminP = prices.index(minP)
#            
#         def isMaxBehindMin(imaxP, iminP):
#             if imaxP > iminP:
#                 return True
#             else:
#                 return False
#                 
#         if isMaxBehindMin(imaxP, iminP):
#             if result > prices[imaxP] - prices[iminP]:
#                 return result
#             else:
#                 result = prices[imaxP] - prices[iminP]
#                 return result
#              
#         else:
#             prices.pop(imaxP)
#             return self.maxProfit(prices)      
# 
# 
# prices = [7, 1, 5, 3, 6, 4]             # 5
# # prices = [7, 1, 5, 3, 9, 6, 4]           # 8
# # prices = [7, 6, 4, 3, 1]            # 0
# # prices = [2,4,1]                    # 2
# # prices = [3,2,6,5,0,3]            # 4
# # prices = [1,2]                      # 1
#  
# so = Solution()
# print so.maxProfit(prices)












# class Solution(object):
#     results = []
#     
#     def maxProfit(self, prices):
#         if len(prices) == 0:
#             return 0
# 
#         lenPrices = len(prices)
#         maxP = max(prices)    
#         minP = min(prices)  
#         imaxP = prices.index(maxP)  
#         iminP = prices.index(minP)
#         
#         maxLeft = prices[:imaxP]
#         try:
#             self.results.append(maxP - min(maxLeft))
#         except ValueError as e:
#             pass
# 
# 
#         # border
#         if iminP == lenPrices-1:
#             prices.pop(-1)
#             if len(prices) == 0:
#                 return 0            
#             minP = min(prices)
#         
#         # border
#         if imaxP == 0:
#             prices.pop(0)
#             if len(prices) == 0:
#                 return 0              
#             maxP = max(prices)
#         
#         imaxP = prices.index(maxP)  
#         iminP = prices.index(minP)
#           
#         def isMaxBehindMin(imaxP, iminP):
#             if imaxP > iminP:
#                 return True
#             else:
#                 return False
#                
#         if isMaxBehindMin(imaxP, iminP):
#             self.results.append(prices[imaxP] - prices[iminP])
#             return max(self.results)
#             
#         else:
#             prices.pop(imaxP)
#             return self.maxProfit(prices)      



# # prices = [7, 1, 5, 3, 6, 4]             # 5
# prices = [7, 1, 5, 3,9, 6, 4]           # 8
# # prices = [7, 6, 4, 3, 1]            # 0
# # prices = [2,4,1]                    # 2
# # prices = [3,2,6,5,0,3]            # 4
# # prices = [1,2]                      # 1
# 
# so = Solution()
# print so.maxProfit(prices)





# class Solution(object):
#     def maxProfit(self, prices):
#         if len(prices) == 0:
#             return 0
#         
#         maxP = max(prices)    
#         minP = min(prices)  
#         imaxP = prices.index(maxP)  
#         iminP = prices.index(minP)
#          
#         def isMaxBehindMin(imaxP, iminP):
#             if imaxP > iminP:
#                 return True
#             else:
#                 return False
#              
#         if isMaxBehindMin(imaxP, iminP):
#             return prices[imaxP] - prices[iminP]
#         else:
#             prices.pop(imaxP)
#             return self.maxProfit(prices)      
    
    











# def maxProfit(prices):
#     if len(prices) == 0:
#         return 0
#     
#     maxP = max(prices)    
#     minP = min(prices)  
#     imaxP = prices.index(maxP)  
#     iminP = prices.index(minP)
#      
#     def isMaxBehindMin(imaxP, iminP):
#         if imaxP > iminP:
#             return True
#         else:
#             return False
#          
#     if isMaxBehindMin(imaxP, iminP):
#         return prices[imaxP] - prices[iminP]
#     else:
#         prices.pop(imaxP)
#         return maxProfit(prices)    
# 
# print maxProfit(prices)



# maxP = max(prices)    
# minP = min(prices)  
# imaxP = prices.index(maxP)  
# iminP = prices.index(minP)
# 
# def isMaxBehindMin(imaxP, iminP):
#     if imaxP > iminP:
#         return True
#     else:
#         return False
#     
# if isMaxBehindMin(imaxP, iminP):
#     return prices[imaxP] - prices[iminP]
# else:
#     prices.pop(imaxP)
#     return prices





# print isMaxBehindMin(imaxP, iminP)
# print prices.pop(iminP), prices



    
    