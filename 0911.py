from langgraph.graph import StateGraph
from typing import TypedDict

# 定义状态
class State(TypedDict):
    user_input: str
    result: str

# 处理节点
def reply_node(state: State):
    msg = state["user_input"]
    return {"result": f"收到你的消息：【{msg}】，LangGraph 简单示例运行成功！"}

# 构建图
workflow = StateGraph(State)
workflow.add_node("reply", reply_node)
workflow.set_entry_point("reply")
workflow.set_finish_point("reply")

app = workflow.compile()

if __name__ == "__main__":
    res = app.invoke({"user_input": "GitHub今日打卡测试"})
    print(res["result"])