# main.py 遗传算法简单寻优实现
import random
import math

# 目标函数：求 f(x) = x*sin(x) 在区间 [0,10] 的最大值
def target_func(x):
    return x * math.sin(x)

class GeneticAlgorithm:
    def __init__(self, pop_size=30, generations=50, cross_rate=0.7, mutate_rate=0.01):
        self.pop_size = pop_size
        self.generations = generations
        self.cross_rate = cross_rate
        self.mutate_rate = mutate_rate
        self.population = []

    def init_population(self):
        """初始化种群"""
        self.population = [random.uniform(0, 10) for _ in range(self.pop_size)]

    def fitness(self, x):
        """适应度"""
        return target_func(x)

    def select(self):
        """轮盘赌选择"""
        fit_list = [self.fitness(ind) for ind in self.population]
        total_fit = sum(fit_list)
        new_pop = []
        for _ in range(self.pop_size):
            r = random.uniform(0, total_fit)
            cur = 0
            for idx, fit in enumerate(fit_list):
                cur += fit
                if cur >= r:
                    new_pop.append(self.population[idx])
                    break
        self.population = new_pop

    def crossover(self):
        """交叉"""
        for i in range(0, self.pop_size - 1, 2):
            if random.random() < self.cross_rate:
                a, b = self.population[i], self.population[i+1]
                alpha = random.random()
                self.population[i] = alpha * a + (1-alpha)*b
                self.population[i+1] = alpha * b + (1-alpha)*a

    def mutate(self):
        """变异"""
        for i in range(self.pop_size):
            if random.random() < self.mutate_rate:
                self.population[i] += random.uniform(-0.3, 0.3)
                self.population[i] = max(0, min(10, self.population[i]))

    def run(self):
        self.init_population()
        best_x = None
        best_fit = -float("inf")
        for g in range(self.generations):
            self.select()
            self.crossover()
            self.mutate()
            # 记录当代最优
            current_best = max(self.population, key=lambda x:self.fitness(x))
            current_fit = self.fitness(current_best)
            if current_fit > best_fit:
                best_fit = current_fit
                best_x = current_best
            print(f"第{g+1}代 | 最优x={best_x:.3f}, 函数值={best_fit:.3f}")
        return best_x, best_fit


if __name__ == "__main__":
    ga = GeneticAlgorithm()
    best_x, best_val = ga.run()
    print("\n====结果====")
    print(f"最优解x = {best_x:.3f}，max(x*sin(x)) = {best_val:.3f}")