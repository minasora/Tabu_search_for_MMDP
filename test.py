import numpy as np
import random




class Solution:
    value = 0
    select_set = []
    unselect_set = []

    def set_value(self, cost_mariax):  # 获得解的目标函数值
        for i in self.select_set:
            for j in self.select_set:
                self.value += cost_mariax[i][j]
        self.value = self.value / 2


def n_add(solution):
    r = random.randint(0, len(solution.unselect_set) - 1)
    solution.select_set.append(solution.unselect_set[r])
    del solution.unselect_set[r]
    solution.set_value(cost_matrix)
    return solution


def n_del(solution):
    r = random.randint(0, solution.select_set.size - 1)
    solution.unselect_set.add(solution.select_set[r])
    del solution.select_set.remove[r]
    solution.set_value(cost_matrix)
    return solution


def n_exchange(solution):
    r_ss = random.randint(0, solution.select_set.size - 1)
    r_uss = random.randint(0, solution.unselect_set.size - 1)
    solution.select_set[r_ss], solution.unselect_set[r_uss] = solution.unselect_set[r_uss], solution.select_set[r_ss]

    # 三种简单邻域操作

    # 两种构建方式：破坏 && 新建


def ini_solution_de():
    new_solution = Solution()
    if_finish = False
    g = []
    for i in range(N):
        new_solution.select_set.append(i)

    while not if_finish:
        for i in new_solution.unselect_set:
            for j in new_solution.select_set:
                g[i] += cost_matrix[i][j]
        index = g[g.index(max(g))]
        if max(g) < 0:
            if_finish = True
        else:
            new_solution.select_set.append(index)
            new_solution.unselect_set.remove(index)
    new_solution.set_value(solution)
    return new_solution


def ini_solution_co():
    new_solution = Solution()
    if_finish = False
    g = []
    for i in range(N):
        new_solution.unselect_set.append(i) #所有的都未选
    n_add(new_solution)
    while not if_finish:
        for i in new_solution.select_set:
            for j in new_solution.unselect_set:
                g.append(cost_matrix[i, j])
        index = g[g.index(min(g))]
        print(g)
        if min(g) < 0:
            if_finish = True
        else:
            new_solution.select_set.append(index)
            new_solution.unselect_set.remove(index)
    new_solution.set_value(cost_matrix)
    return new_solution


f = open("MDPI1_20.txt")
N = 20
cost_matrix = np.zeros((22, 22))
while True:
    line = f.readline()
    if line == "end":
        break
    else:
        a = line.split("\t")
        print(a)
        cost_matrix[int(a[0])-1, int(a[1])-1] = a[2]
        cost_matrix[int(a[1])-1, int(a[0])-1] = a[2]
print(cost_matrix[19, 0])
solution = ini_solution_co()
print(solution.select_set)
print(solution.unselect_set)
