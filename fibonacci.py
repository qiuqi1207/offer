# -*- coding:utf-8 -*-
class Solution:
  def Fibonacci(self,n):
    f0=0
    f1=1
    if n==0:
        return 0
    if n==1:
        return 1
    for i in range(n-1):
        a=f0
        f0=f1
        f1=f1+a
    return f1