# -*- coding: utf-8 -*-


class Solution:
    """
    基本思路：上三角和下三角
    1.构造n*n数组--将数组行向扩展n-1次，所要的结果就是每行不包括斜对称轴上的元素的成绩构成的一个新数组
    2.上面的二维数组又可以分为两个三角，先求下三角再求上三角，每行的结果相乘
    """
    # 27ms 5752k
    def multiply(self, A):
        n = len(A)
        B = [1] * len(A)

        # 下三角
        """
        A1
        A1*A2
        A1*A2*A3
        :
        :
        A1*A2*A3...A(n-2)
        """
        tmp = 1
        for i in range(1, n):
            tmp *= A[i-1]
            B[i] *= tmp

        # 上三角
        """
        A1A2A3......A(n-2)A(n-1)
                               :
                               :
              A(n-3)A(n-2)A(n-1)
                    A(n-2)A(n-1)
                          A(n-1)
        """
        tmp = 1
        for i in range(n - 2, -1, -1):
            tmp *= A[i+1]
            B[i] *= tmp

        return B
