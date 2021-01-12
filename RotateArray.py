# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
      right=len(rotateArray)-1
      left=0
      while(left<right):
        mid=(left+right)/2
        if right-left==1:
            return rotateArray[right]
        elif rotateArray[mid]>rotateArray[right]:
            left=mid
        elif rotateArray[left]>rotateArray[mid]:
            right=mid
      
            
        