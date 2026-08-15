import numpy as np

class PSO:
    def __init__(self, func, dim, pop_num=30, max_iter=50, w=0.5, c1=2, c2=2):
        """
        :param func: 目标优化函数
        :param dim: 变量维度
        :param pop_num: 粒子数量
        :param max_iter: 最大迭代次数
        :param w: 惯性权重
        :param c1: 个体学习因子
        :param c2: 全局学习因子
        """
        self.func = func
        self.dim = dim
        self.pop_num = pop_num
        self.max_iter = max_iter
        self.w = w
        self.c1 = c1
        self.c2 = c2

        # 初始化粒子位置、速度
        self.pos = np.random.rand(pop_num, dim) * 10 - 5
        self.vel = np.random.rand(pop_num, dim) * 2

        self.pbest_pos = self.pos.copy()
        self.pbest_val = np.array([self.func(p) for p in self.pos])
        self.gbest_idx = np.argmin(self.pbest_val)
        self.gbest_pos = self.pbest_pos[self.gbest_idx].copy()
        self.gbest_val = self.pbest_val[self.gbest_idx]

    def iterate(self):
        history = []
        for t in range(self.max_iter):
            for i in range(self.pop_num):
                # 更新速度
                r1 = np.random.random()
                r2 = np.random.random()
                self.vel[i] = (self.w * self.vel[i]
                               + self.c1 * r1 * (self.pbest_pos[i] - self.pos[i])
                               + self.c2 * r2 * (self.gbest_pos - self.pos[i]))
                # 更新位置
                self.pos[i] += self.vel[i]
                # 更新个体最优
                current_val = self.func(self.pos[i])
                if current_val < self.pbest_val[i]:
                    self.pbest_val[i] = current_val
                    self.pbest_pos[i] = self.pos[i].copy()
                    if current_val < self.gbest_val:
                        self.gbest_val = current_val
                        self.gbest_pos = self.pos[i].copy()
            history.append(self.gbest_val)
            print(f"迭代{t+1:2d} | 全局最优值：{self.gbest_val:.4f}")
        return self.gbest_pos, self.gbest_val, history


# 测试目标函数：Sphere函数
def sphere(x):
    return np.sum(x ** 2)


if __name__ == "__main__":
    print("=====粒子群优化PSO测试=====")
    pso = PSO(sphere, dim=2)
    best_pos, best_val, record = pso.iterate()
    print(f"\n最优解位置：{best_pos}")
    print(f"最优函数值：{best_val:.4f}")