import os
from dotenv import load_dotenv
from langchain_community.chat_models import ChatTongyi

load_dotenv(override=False)

# 初始化 deepseek
model = ChatTongyi(
    model="qwen-turbo",
    temperature=0,
    api_key=os.getenv("QWEN_API_KEY"),
)

# 打印结果
print(model.invoke("什么是LangChain?").content)
