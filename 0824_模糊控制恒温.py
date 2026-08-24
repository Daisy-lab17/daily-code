import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

# ====================== 1. 定义输入输出模糊变量 ======================
# 输入1：温度误差（设定25℃，范围-10 ~ 10）
temp_err = ctrl.Antecedent(np.arange(-10, 11, 1), 'temp_error')
# 输入2：误差变化率（单位时间温度变化，-5 ~ 5）
err_change = ctrl.Antecedent(np.arange(-5, 6, 1), 'error_change')
# 输出：加热功率（0 ~ 100）
heat_power = ctrl.Consequent(np.arange(0, 101, 1), 'heat_power')

# 定义误差隶属度函数
temp_err['negative_big'] = fuzz.trimf(temp_err.universe, [-10, -10, -3])
temp_err['negative_small'] = fuzz.trimf(temp_err.universe, [-6, -3, 0])
temp_err['zero'] = fuzz.trimf(temp_err.universe, [-2, 0, 2])
temp_err['positive_small'] = fuzz.trimf(temp_err.universe, [0, 3, 6])
temp_err['positive_big'] = fuzz.trimf(temp_err.universe, [3, 10, 10])

# 定义误差变化率隶属度函数
err_change['down_fast'] = fuzz.trimf(err_change.universe, [-5, -5, -2])
err_change['down_slow'] = fuzz.trimf(err_change.universe, [-3, -1, 0])
err_change['stable'] = fuzz.trimf(err_change.universe, [-1, 0, 1])
err_change['up_slow'] = fuzz.trimf(err_change.universe, [0, 1, 3])
err_change['up_fast'] = fuzz.trimf(err_change.universe, [2, 5, 5])

# 定义加热功率隶属度函数
heat_power['stop'] = fuzz.trimf(heat_power.universe, [0, 0, 20])
heat_power['low'] = fuzz.trimf(heat_power.universe, [10, 30, 50])
heat_power['mid'] = fuzz.trimf(heat_power.universe, [40, 60, 80])
heat_power['high'] = fuzz.trimf(heat_power.universe, [70, 100, 100])

# ====================== 2. 模糊控制规则库 ======================
rule1 = ctrl.Rule(temp_err['negative_big'] & err_change['down_fast'], heat_power['high'])
rule2 = ctrl.Rule(temp_err['negative_big'] & err_change['stable'], heat_power['high'])
rule3 = ctrl.Rule(temp_err['negative_small'] & err_change['stable'], heat_power['mid'])
rule4 = ctrl.Rule(temp_err['zero'] & err_change['stable'], heat_power['low'])
rule5 = ctrl.Rule(temp_err['positive_small'] & err_change['up_slow'], heat_power['stop'])
rule6 = ctrl.Rule(temp_err['positive_big'] & err_change['up_fast'], heat_power['stop'])

# 构建控制系统
temp_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
sim = ctrl.ControlSystemSimulation(temp_ctrl)

# ====================== 3. 仿真测试 ======================
def run_simulation(target_temp=25, current_temp=18, delta_t=0.1, total_time=60):
    time_list = []
    temp_list = []
    power_list = []
    t = 0
    temp = current_temp
    while t < total_time:
        error = target_temp - temp
        d_err = (target_temp - temp) - (target_temp - temp_list[-1] if len(temp_list) > 0 else error)
        sim.input['temp_error'] = error
        sim.input['error_change'] = d_err
        sim.compute()
        power = sim.output['heat_power']
        # 温度模拟升温模型
        temp += power * 0.025 - 0.08
        time_list.append(t)
        temp_list.append(temp)
        power_list.append(power)
        t += delta_t
    # 绘图
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.plot(time_list, temp_list, label='实际温度')
    plt.axhline(target_temp, color='r', linestyle='--', label='目标25℃')
    plt.title('温度响应曲线')
    plt.xlabel('时间(s)')
    plt.ylabel('温度(℃)')
    plt.legend()
    plt.grid(True)
    plt.subplot(122)
    plt.plot(time_list, power_list, color='orange')
    plt.title('模糊控制输出加热功率')
    plt.xlabel('时间(s)')
    plt.ylabel('功率(%)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    return temp_list, power_list

if __name__ == "__main__":
    print("=== 模糊控制恒温系统仿真 ===")
    temp_data, power_data = run_simulation(target_temp=25, current_temp=16)
    print(f"稳态最终温度：{temp_data[-1]:.2f} ℃")
    print(f"稳态加热功率：{power_data[-1]:.2f} %")