# -*- coding: utf-8 -*-


class Solution:

    """
    基本思路：二维数组是有序的（行递增、列递增），那么就可以从右上角开始（或左下角）开始与目标数字对比
        1.设定一个初始位置在右上角（array[0][len(array[0]) - 1]）的移动点
        2.比目标大，那么移动点的列数就左移
        3.比目标校，那么移动电的行数就下移
        4.对比出相同的就输出True，否则就输出False
    """

    def find_int_number(self, target, array):
        i = 0
        j = len(array[0]) - 1
        while i <= len(array) - 1 and j >= 0:
            current_ay = array[i][j]
            if current_ay > target:
                j -= 1
            elif current_ay < target:
                i += 1
            else:
                return True
