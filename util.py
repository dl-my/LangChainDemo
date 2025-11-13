import os, dotenv
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()


# 初始化聊天模型
def get_model(model_name: str = "qwen3-max") -> ChatOpenAI:
    return ChatOpenAI(
        model=model_name,
        api_key=os.getenv("DASHSCOPE_API_KEY"),
        base_url=os.getenv("DASHSCOPE_BASE_URL"),
    )
