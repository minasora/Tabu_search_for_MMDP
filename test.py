import numpy as np
import random
cost_mariax = []

class Solution:
    value = 0
    select_set = []
    unselect_set = []
    def set_value(self, cost_mariax):#获得解的目标函数值
        for i in select_set:
            for j in select_set:
                self.value += cost_mariax[i][j]
        self.value = self.value/2


def n_add(solution):
    r = random.randint(0, solution.unselect_set.size-1)
    solution.select_set.add(solution.unselect_set[r])
    del solution.unselect_set.remove[r]
    solution.set_value(cost_mariax)
    return solution


def n_del(solution):
    r = random.randint(0, solution.select_set.size-1)
    solution.unselect_set.add(solution.select_set[r])
    del solution.select_set.remove[r]
    solution.set_value(cost_mariax)
    return solution
def n_exchange(solution):
    r_ss = random.randint(0,solution.select_set.size-1)
    r_uss = random.randint(0,solution.unselect_set.size-1)
    solution.select_set[r_ss],solution.unselect_set[r_uss] = solution.unselect_set[r_uss],solution.select_set[r_ss]
#三种简单邻域操作


def ini_solution_de:


def ini_solution_co: