import numpy as np
import matplotlib.pyplot as plt

# 二阶被控对象，相当于你的电机/控制系统
def system(y, u, dt):
    dy = -2 * y + u
    return y + dy * dt

# --------普通PID（参数固定死不变）--------
def pid_calc(err, err_sum, err_last, kp, ki, kd, dt):
    err_sum = err_sum + err * dt
    dedt = (err - err_last)/dt
    u = kp*err + ki*err_sum + kd*dedt
    return u, err_sum

# --------模糊PID（简化：根据误差动态修改Kp）--------
def fuzzy_adjust(e):
    """简化模糊规则：误差大，加大kp；误差小，减小kp"""
    e = np.clip(e, -1, 1)
    dkp = 3 * abs(e)
    dki = 0.3 * abs(e)
    dkd = 0.1 * abs(e)
    return dkp, dki, dkd


# =========仿真开始==========
dt = 0.01
time_total = 10
t = np.arange(0, time_total, dt)
N = len(t)
setpoint = 1    #目标值阶跃输入

#=====普通PID仿真
y_pid = np.zeros(N)
sum_e = 0
e_last = 0
kp1,ki1,kd1 = 8,2.5,1.2
for i in range(1,N):
    e = setpoint - y_pid[i‑1]
    u, sum_e = pid_calc(e, sum_e, e_last, kp1,ki1,kd1, dt)
    y_pid[i] = system(y_pid[i‑1], u, dt)
    e_last = e

#=====模糊自整定PID仿真
y_fuzzy = np.zeros(N)
sum_e2 = 0
e_last2 = 0
kp0,ki0,kd0 = 8,2.5,1.2

for i in range(1,N):
    e = setpoint - y_fuzzy[i‑1]
    ec = (e‑e_last2)/dt
    # 模糊输出，修正PID参数
    dkp,dki,dkd = fuzzy_adjust(e)
    kp = kp0 + dkp
    ki = ki0 + dki
    kd = kd0 + dkd

    sum_e2 += e*dt
    dedt = (e‑e_last2)/dt
    u = kp*e + ki*sum_e2 + kd*dedt
    y_fuzzy[i] = system(y_fuzzy[i‑1], u, dt)
    e_last2 = e


# 画图对比
plt.figure(dpi=120)
plt.plot(t,y_pid,'r‑',label='普通PID')
plt.plot(t,y_fuzzy,'b‑',label='模糊PID')
plt.grid(True)
plt.legend()
plt.xlabel('时间 s')
plt.ylabel('输出')
plt.title('PID与模糊PID阶跃响应对比')
plt.show()