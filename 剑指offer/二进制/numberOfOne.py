from ctypes import *


class Solution:
	def number(self, n):
		cnt = 0
		while c_int(n).value:
			n = n-1 & n
			cnt += 1
		return cnt
