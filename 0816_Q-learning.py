import numpy as np

class MazeEnv:
    """4×4简易迷宫环境"""
    def __init__(self):
        self.size = 4
        self.start = 0
        self.end = 15
        # 障碍物格子编号
        self.obstacle = [5,6,9,10]

    def reset(self):
        self.state = self.start
        return self.state

    def step(self, action):
        """
        action: 0上 1下 2左 3右
        return next_state, reward, done
        """
        r = self.state // self.size
        c = self.state % self.size

        if action == 0:
            nr, nc = r-1, c
        elif action == 1:
            nr, nc = r+1, c
        elif action == 2:
            nr, nc = r, c-1
        else:
            nr, nc = r, c+1

        # 边界约束
        if nr < 0 or nr >= self.size or nc <0 or nc >= self.size:
            next_state = self.state
        else:
            next_state = nr * self.size + nc
            if next_state in self.obstacle:
                next_state = self.state

        # 奖励设置
        if next_state == self.end:
            reward = 100
            done = True
        else:
            reward = -1
            done = False

        self.state = next_state
        return next_state, reward, done


class QLearningAgent:
    def __init__(self, state_num, act_num, lr=0.1, gamma=0.9, eps=0.2):
        self.lr = lr          # 学习率
        self.gamma = gamma    # 折扣因子
        self.eps = eps        # 探索率ε‑greedy
        self.q_table = np.zeros((state_num, act_num))

    def choose_action(self, state):
        if np.random.rand() < self.eps:
            return np.random.randint(0,4)
        else:
            return np.argmax(self.q_table[state])

    def update(self, s, a, r, s_next):
        q_target = r + self.gamma * np.max(self.q_table[s_next])
        self.q_table[s,a] += self.lr * (q_target - self.q_table[s,a])


if __name__ == "__main__":
    env = MazeEnv()
    agent = QLearningAgent(state_num=16, act_num=4)
    episode = 200

    print("=====Q‑Learning迷宫训练开始=====")
    for ep in range(episode):
        s = env.reset()
        total_reward = 0
        while True:
            a = agent.choose_action(s)
            s_n, r, done = env.step(a)
            agent.update(s,a,r,s_n)
            s = s_n
            total_reward += r
            if done:
                break
        if (ep+1) % 20 == 0:
            print(f"回合{ep+1:3d} | 累计奖励:{total_reward}")

    print("\n训练完成Q表：")
    print(agent.q_table)