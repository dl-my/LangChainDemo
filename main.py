import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi

load_dotenv()

# 初始化模型
model = ChatTongyi(
    model="qwen-turbo",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
)

# 打印结果
print(model.invoke("什么是LangChain?").content)
