import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage

load_dotenv()

# 初始化模型
model = ChatTongyi(
    model="qwen-turbo",
    temperature=0,
    api_key=os.getenv("DASHSCOPE_API_KEY"),
)

""" # 1 直接调用
print(model.invoke("什么是LangChain?").content) """

# 2 模型调用方法
""" # 2.1 对话模型
messages = [
    SystemMessage(content="你叫小亮，是一个乐于助人的人工助手"),
    HumanMessage(content="你是谁"),
]
response = model.invoke(messages)
print(response.content)
print(type(response)) """

""" # 2.2 流式输出
messages = [
    SystemMessage(content="你叫小亮，是一个乐于助人的人工助手"),
    HumanMessage(content="你是谁"),
]
response = model.stream(messages)
# 流式打印结果
for chunk in response:
    print(
        chunk.content, end="", flush=True
    )  # 刷新缓冲区 (无换行符，缓冲区未刷新，内容可能不会立即显示)
print("\n")
print(type(response)) """

""" # 2.3 批量调用
# 问题列表
questions = [
    "什么是LangChain？",
    "Python的生成器是做什么的？",
    "解释一下Docker和Kubernetes的关系",
]
# 批量调用大模型
response = model.batch(questions)
for q, r in zip(questions, response):
    print(f"问题：{q}\n回答：{r}\n") """

""" # 2.4 异步调用
import asyncio


async def main():
    # 异步调用一条请求
    response = await model.ainvoke("解释一下LangChain是什么")
    print(response)


# 运行异步程序的入口点
asyncio.run(main()) """
