# -*- coding: utf-8 -*-
import collections


class Solution(object):

    """
    方法1：数组切片-每次遍历一个数，将它前、后的数用切片重新组成一个数组，判断当前的数是否在其中
    方法2：集合-每次从数组中取出一个数，加入空的集合中，检测集合的长度变化，如果加入后长度未变，则当前加入的数就是重复数
    方法3：collections_频率统计：利用collections.Counter()统计所有数字成员出现的频率，遍历获取第一频率大于1的及时重复数
    """
    # 25ms 5624k
    def duplicate_1(self, numbers, duplication):
        for i in range(len(numbers)):
            currentNUm = numbers[i]
            fontNums = numbers[:i]
            backNums = numbers[i+1:]
            otherNums = fontNums + backNums
            if currentNUm in otherNums:
                duplication[0] = currentNUm
                return True
        return False

    # 28 5624k
    def duplicate_2(self, numbers, duplication):
        tempSet = set()
        length = 0
        for i in range(len(numbers)):
            length += 1
            tempSet.add(numbers[i])
            if length > len(tempSet):
                duplication[0] = numbers[i]
                return True
        return False

    # 42ms 5624k
    def duplicate_3(self, numbers, duplication):
        a = collections.Counter(numbers)
        for k,v in a.items():
            if v > 1:
                duplication[0] = k
                return True
        return False
