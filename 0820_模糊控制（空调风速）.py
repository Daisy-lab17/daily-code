# 智能控制-模糊控制示例，适配课程知识点
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# 1. 定义输入变量：温度 0~40℃
temperature = ctrl.Antecedent(np.arange(0, 41, 1), "temperature")
# 输出变量：空调风速 0~100档
fan_speed = ctrl.Consequent(np.arange(0, 101, 1), "fan_speed")

# 2. 划分模糊集合：冷、舒适、热
temperature.automf(3, names=["cold", "comfortable", "hot"])
fan_speed.automf(3, names=["low", "medium", "high"])

# 3. 人工专家控制规则
rule1 = ctrl.Rule(temperature["cold"], fan_speed["low"])
rule2 = ctrl.Rule(temperature["comfortable"], fan_speed["medium"])
rule3 = ctrl.Rule(temperature["hot"], fan_speed["high"])

# 4. 搭建模糊控制系统
fan_ctrl_system = ctrl.ControlSystem([rule1, rule2, rule3])
sim = ctrl.ControlSystemSimulation(fan_ctrl_system)

# 测试1：低温 12℃
sim.input["temperature"] = 12
sim.compute()
print(f"温度12℃，空调风速：{sim.output['fan_speed']:.2f}")

# 测试2：适宜温度 26℃
sim.input["temperature"] = 26
sim.compute()
print(f"温度26℃，空调风速：{sim.output['fan_speed']:.2f}")

# 测试3：高温 36℃
sim.input["temperature"] = 36
sim.compute()
print(f"温度36℃，空调风速：{sim.output['fan_speed']:.2f}")