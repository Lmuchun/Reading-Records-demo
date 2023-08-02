# -*- coding: utf-8 -*-
"""MyProblem.py"""
import numpy as np
import geatpy as ea


class MyProblem(ea.Problem):  # 继承Problem父类
    def __init__(self):

        name = 'MyProblem'  # 初始化name（函数名称，可以随意设置）
        M = 1  # 初始化M（目标维数）
        maxormins = [-1]  # 初始化目标最小最大化标记列表，1：min；-1：max
        Dim = 8  # 初始化Dim（决策变量维数）
        varTypes = [0] * Dim  # 初始化决策变量类型，0：连续；1：离散
        lb = [25954, 82026, 67074.6, 3538.1,
              245.1, 2065.9, 1483.3, 911.4]  # 决策变量下界
        ub = [28666.6, 190516, 190516, 3585.2,
              443.6, 2994.3, 2158.3, 956.8]  # 决策变量上界
        lbin = [1, 1, 1, 1, 1, 1, 1, 1]  # 决策变量下边界
        # lbin = [0, 0, 1, 0, 0, 0, 0, 0]  # 决策变量下边界
        ubin = [0, 0, 0, 0, 0, 0, 0, 0]  # 决策变量上边界
        # 调用父类构造方法完成实例化
        ea.Problem.__init__(self, name, M, maxormins, Dim, varTypes, lb,
                            ub, lbin, ubin)

    def aimFunc(self, pop):  # 目标函数，pop为传入的种群对象

        Vars = pop.Phen  # 得到决策变量矩阵
        x1 = Vars[:, [0]]  # 取出第一列得到所有个体的x1组成的列向量
        x2 = Vars[:, [1]]  # 取出第二列得到所有个体的x2组成的列向量
        x3 = Vars[:, [2]]  # 取出第三列得到所有个体的x3组成的列向量
        x4 = Vars[:, [3]]
        x5 = Vars[:, [4]]
        x6 = Vars[:, [5]]
        x7 = Vars[:, [6]]
        x8 = Vars[:, [7]]
        # 计算目标函数值，赋值给pop种群对象的ObjV属性
        pop.ObjV = 3961.6*x1 + 19774.9*x2 + 15613.5*x3 + 126128.5 * \
            x4 - 9607.9*x5 - 9607.9*x6 - 9607.9*x7 + 210.8*x8
        # 采用可行性法则处理约束，生成种群个体违反约束程度矩阵
        pop.CV = np.hstack(
            [np.abs(x1 + x2 + x3 + x4 + x5 + x6 + x7 + x8 - 190516)])  # 第三个约束
