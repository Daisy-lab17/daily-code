# main.py  基于Sarsa强化学习迷宫小游戏
import numpy as np
import random

# 迷宫环境 0通路 1墙 2终点
maze = np.array([
    [0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 1, 2]
])

actions = ["up", "down", "left", "right"]
# Q表
Q = np.zeros((maze.shape[0], maze.shape[1], len(actions)))

alpha = 0.1    #学习率
gamma = 0.9    #折扣因子
epsilon = 0.1  #探索概率
episodes = 300

def get_next_state(state, act):
    r, c = state
    if act == "up":
        nr, nc = r-1, c
    elif act == "down":
        nr, nc = r+1, c
    elif act == "left":
        nr, nc = r, c-1
    else:
        nr, nc = r, c+1
    #撞墙或者越界，原地不动
    if nr<0 or nr>=5 or nc<0 or nc>=5 or maze[nr,nc]==1:
        return r,c
    return nr, nc

def get_reward(state):
    r,c = state
    if maze[r,c]==2:
        return 100
    return -1

def choose_action(state):
    r,c = state
    if random.uniform(0,1) < epsilon:
        return random.choice(actions)
    else:
        idx = np.argmax(Q[r,c,:])
        return actions[idx]

# Sarsa主循环
for ep in range(episodes):
    s = (0,0)
    a = choose_action(s)
    while True:
        s_next = get_next_state(s,a)
        r = get_reward(s_next)
        a_next = choose_action(s_next)
        ai = actions.index(a)
        ai_next = actions.index(a_next)
        #Sarsa更新公式
        Q[s[0],s[1],ai] += alpha*(r + gamma*Q[s_next[0],s_next[1],ai_next] - Q[s[0],s[1],ai])
        s,a = s_next,a_next
        if maze[s]==2:
            break

#测试运行
def run_test():
    pos = (0,0)
    path = [pos]
    while maze[pos] !=2:
        act = choose_action(pos)
        pos = get_next_state(pos,act)
        path.append(pos)
    print("找到目标路径：",path)
    return path

if __name__ == "__main__":
    print("Sarsa强化学习迷宫训练完成")
    run_test()