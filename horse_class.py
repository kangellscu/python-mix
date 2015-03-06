#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import copy


class HorseJump():
    """
    题目:
    一个棋盘有 8*8=64 个格子，编号 (1,1), (1,2), …… (8,8)。 
    “马”按照“日”字走法 从指定起点跳到指定终点，写一程序求最短路径需要几步。
    例如，从(1,1)点跳到 (4,4)点至少要两步，一种方式为 (1,1) -> (2,3) -> (4,4)。
    程序接受４个 1-8 之间整 数，表示起点和终点位置，计算出最短路径需要几步

    思路:
    采用递归方式，穷举所有可能的路线，当下一跳出现异常(跳出棋盘，已经在路线中)
    或者达到目标坐标时，回退到上一跳，检查其余分支。为了减少递归次数，
    使用self.min_path，当成功到达目标坐标时，将当前路线记录到self.min_path中，
    之后的路线尝试不超过self.min_path的坐标数

    >>> o = HorseJump()
    >>> o.run((3,3), (1, 2))
    >>> print o.min_path
    [(3, 3), (1, 2)]
    """

    min_path = []
    path = []
    path_list = []
    target_location = ()

    next_rule = {
        0: lambda x, y: (x + 1, y + 2),
        1: lambda x, y: (x + 2, y + 1),
        2: lambda x, y: (x + 2, y - 1),
        3: lambda x, y: (x + 1, y - 2),
        4: lambda x, y: (x - 1, y - 2),
        5: lambda x, y: (x - 2, y - 1),
        6: lambda x, y: (x - 2, y + 1),
        7: lambda x, y: (x - 1, y + 2),
        }

    def __init__(self, scale=8):
        self.rows = self.cols = scale 


    def __init(self):
        self.min_path = []
        self.path = []
        self.path_list = []


    def run(self, begin_location, target_location):
        self.__init()
        self.begin_location = begin_location
        self.target_location = target_location
        self.jump(self.begin_location)

        return self


    def jump(self, curr_location):
        """
        采用递归的方式处理，在出现异常，达到终点等场景下，回退到上一跳
        使用 self.min_path 减少递归的次数
        """

        curr_x, curr_y = curr_location

        if (curr_x, curr_y) in self.path:
            return

        self.path.append(curr_location)

        if len(self.min_path) > 0 and len(self.path) >= len(self.min_path):
            self.__jump_back()
            return

        if curr_x < 0 or curr_x >= self.rows \
            or curr_y < 0 or curr_y >= self.cols:
                self.__jump_back()
                return

        if self.__is_finished(curr_location):
            self.__handle_finish()
            self.__jump_back()
            return

        for direction_index in self.next_rule.keys():
            next_location = self.__get_next_location(curr_location, direction_index)
            self.jump(next_location)

        self.__jump_back()


    def __get_next_location(self, curr_location, direction_index):
        """
        计算下一跳坐标，每个坐标有8个可能的起跳方向
        """
        curr_x, curr_y = curr_location
        if direction_index not in self.next_rule.keys():
            return [-1, -1]
        
        return self.next_rule[direction_index](curr_x, curr_y)


    def __jump_back(self):
        if len(self.path):
            self.path.pop()


    def __is_finished(self, curr_location):
        return curr_location == self.target_location


    def __handle_finish(self):
        finished_path = copy.deepcopy(self.path)
        if len(self.min_path) == 0 or len(finished_path) < len(self.min_path):
            self.min_path = finished_path
        self.path_list.append(finished_path)



if __name__ == "__main__":
    horse = HorseJump()
    horse.run((0, 0), (2, 1))
    print len(horse.min_path)
