import numpy as np
import matplotlib.pyplot as plt

# Sigmoid激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# BP神经网络：输出PID三个参数Kp、Ki、Kd
class NeuralNetPID:
    def __init__(self, in_dim=3, hidden_dim=6, out_dim=3):
        # 权重初始化
        self.W1 = np.random.randn(in_dim, hidden_dim) * 0.1
        self.b1 = np.zeros(hidden_dim)
        self.W2 = np.random.randn(hidden_dim, out_dim) * 0.1
        self.b2 = np.zeros(out_dim)

    def forward(self, x):
        # 前向传播
        z1 = np.dot(x, self.W1) + self.b1
        a1 = sigmoid(z1)
        z2 = np.dot(a1, self.W2) + self.b2
        out = sigmoid(z2)
        # 映射到合理PID参数区间 [0,10]
        return out * 10

# 传统PID控制器
class PID:
    def __init__(self):
        self.integral = 0.0
        self.last_err = 0.0

    def calculate(self, err, dt, Kp, Ki, Kd):
        self.integral += err * dt
        diff = (err - self.last_err) / dt
        u = Kp * err + Ki * self.integral + Kd * diff
        self.last_err = err
        return u

# 被控对象：一阶惯性环节 G(s)=1/(Ts+1)
def plant(u, y_last, T=0.8, dt=0.01):
    y = y_last + dt * (u - y_last) / T
    return y

if __name__ == "__main__":
    nn = NeuralNetPID()
    pid = PID()
    dt = 0.01
    total_time = 10
    steps = int(total_time / dt)
    target = 1.0  # 设定值
    y = 0.0       # 系统初始输出

    record_y = []
    record_t = []

    for i in range(steps):
        t = i * dt
        err = target - y
        # 神经网络输入：误差、误差积分、误差微分
        x = np.array([err, pid.integral, err - pid.last_err])
        Kp, Ki, Kd = nn.forward(x)
        # PID输出控制量
        u = pid.calculate(err, dt, Kp, Ki, Kd)
        # 被控对象迭代
        y = plant(u, y)

        record_t.append(t)
        record_y.append(y)

    # 绘图
    plt.figure(figsize=(8,4))
    plt.plot(record_t, record_y, label="系统输出", linewidth=2)
    plt.axhline(target, color="r", linestyle="--", label="设定值1.0")
    plt.xlabel("时间 t")
    plt.ylabel("输出 y")
    plt.title("神经网络自适应PID控制仿真")
    plt.legend()
    plt.grid()
    plt.show()
