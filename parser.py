import os, dotenv
from loguru import logger
from langchain_openai import ChatOpenAI

dotenv.load_dotenv()
# 初始化聊天模型
model = ChatOpenAI(
    model="qwen3-max",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url=os.getenv("DASHSCOPE_BASE_URL"),
)

### 输出解析器
#### 常见输出解析器用法
""" # 字符串解析器
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# 创建聊天提示模板，包含系统角色设定和用户问题输入
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role},请简短回答我提出的问题"),
        ("human", "请回答:{question}"),
    ]
)

# 使用指定的角色和问题生成具体的提示内容
prompt = chat_prompt.invoke({"role": "AI助手", "question": "什么是LangChain"})
logger.info(prompt)

# 调用模型获取回答结果
result = model.invoke(prompt)
logger.info(f"模型原始输出:\n{result}")

# 创建字符串输出解析器，用于解析模型返回的结果
parser = StrOutputParser()

# 打印解析后的结构化结果
response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")

# 打印类型
logger.info(f"结果类型: {type(response)}") """

""" # Json解析器
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# 创建聊天提示模板，包含系统角色设定和用户问题输入
chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "你是一个{role},请简短回答我提出的问题,结果返回严格的json格式,q字段表示问题,a字段表示答案。",
        ),
        ("human", "请回答:{question}"),
    ]
)

# 使用指定的角色和问题生成具体的提示内容
prompt = chat_prompt.invoke({"role": "AI助手", "question": "什么是LangChain"})
logger.info(prompt)

# 调用模型获取回答结果
result = model.invoke(prompt)
logger.info(f"模型原始输出:\n{result}")

# 创建Json输出解析器实例
parser = JsonOutputParser()

# 调用解析器处理结果数据，将输入转换为JSON格式的响应
response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")

# 打印类型
logger.info(f"结果类型: {type(response)}") """

""" # 使用get_format_instructions 生成格式说明
from pydantic import BaseModel, Field
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser


class Person(BaseModel):

    # 定义一个新闻结构化的数据模型类
    # 属性:
    #     time (str): 新闻发生的时间
    #     person (str): 新闻涉及的人物
    #     event (str): 发生的具体事件

    time: str = Field(description="时间")
    person: str = Field(description="人物")
    event: str = Field(description="事件")


# 创建JSON输出解析器，用于将model输出解析为Person对象
parser = JsonOutputParser(pydantic_object=Person)

# 获取格式化指令，告诉model如何输出符合要求的JSON格式
format_instructions = parser.get_format_instructions()

# 创建聊天提示模板，定义系统角色和用户输入格式
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手，你只能输出结构化JSON数据。"),
        ("human", "请生成一个关于{topic}的新闻。{format_instructions}"),
    ]
)

# 格式化提示词，填入具体主题和格式化指令
prompt = chat_prompt.format_messages(
    topic="小米", format_instructions=format_instructions
)

# 记录格式化后的提示词信息
logger.info(prompt)

# 调用大语言模型获取响应结果
result = model.invoke(prompt)

# 记录模型返回的结果
logger.info(f"模型原始输出:\n{result}")

# 使用解析器将模型输出解析为结构化数据
response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")

# 打印类型
logger.info(f"结果类型: {type(response)}") """

""" # 列表解析器
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import CommaSeparatedListOutputParser

# 创建逗号分隔列表输出解析器实例
parser = CommaSeparatedListOutputParser()

# 获取格式化指令，用于指导模型输出格式
format_instructions = parser.get_format_instructions()

# 创建聊天提示模板，包含系统消息和人类消息
# 系统消息定义了AI助手的行为规范和输出格式要求
# 人类消息定义了具体的任务请求，使用占位符{topic}表示主题
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", f"你是一个AI助手，你只能输出结构化列表数据。{format_instructions}"),
        ("human", "请生成5个关于{topic}的内容"),
    ]
)

# 格式化聊天提示消息，将占位符替换为实际值
prompt = chat_prompt.format_messages(
    topic="小米", format_instructions=format_instructions
)

# 记录格式化后的提示消息
logger.info(prompt)

# 调用模型执行推理，传入格式化的提示消息
result = model.invoke(prompt)

# 记录模型返回的原始结果
logger.info(f"模型原始输出:\n{result}")

# 使用解析器处理模型返回的结果，将其转换为结构化列表
response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")

# 打印类型
logger.info(f"结果类型: {type(response)}") """

""" # XML 解析器
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import XMLOutputParser

# 创建 XML 输出解析器实例
parser = XMLOutputParser()

# 获取格式化指令（这会告诉模型如何以 XML 格式输出）
format_instructions = parser.get_format_instructions()

# 创建提示模板
chat_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            f"你是一个AI助手，只能输出XML格式的结构化数据。{format_instructions}",
        ),
        (
            "human",
            "请生成5个关于{topic}的内容，每个内容包含<name>和<description>两个字段",
        ),
    ]
)

# 格式化提示，将 {topic} 替换为实际主题
prompt = chat_prompt.format_messages(
    topic="小米", format_instructions=format_instructions
)

# 打印提示消息
logger.info(prompt)

# 执行推理
result = model.invoke(prompt)

# 记录模型原始输出
logger.info(f"模型原始输出:\n{result.content}")

# 解析 XML 输出为结构化 Python 对象（例如字典或列表）
response = parser.invoke(result)

# 打印解析后的结构化结果
logger.info(f"解析后的结构化结果:\n{response}")

# 打印类型
logger.info(f"结果类型: {type(response)}") """

### 解析器进阶用法
# Pydantic解析器
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field, field_validator
from langchain_core.output_parsers import PydanticOutputParser


class Product(BaseModel):
    """
    产品信息模型类，用于定义产品的结构化数据格式

    属性:
        name (str): 产品名称
        category (str): 产品类别
        description (str): 产品简介，长度必须大于等于10个字符
    """

    name: str = Field(description="产品名称")
    category: str = Field(description="产品类别")
    description: str = Field(description="产品简介")

    @field_validator("description")
    def validate_description(cls, value):
        """
        验证产品简介字段的长度

        参数:
            value (str): 待验证的产品简介文本

        返回:
            str: 验证通过的产品简介文本

        异常:
            ValueError: 当产品简介长度小于10个字符时抛出
        """
        if len(value) < 10:
            raise ValueError("产品简介长度必须大于等于10")
        return value


# 创建Pydantic输出解析器实例，用于解析模型输出为Product对象
parser = PydanticOutputParser(pydantic_object=Product)

# 获取格式化指令，用于指导模型输出符合Product模型的JSON格式
format_instructions = parser.get_format_instructions()

# 创建聊天提示模板，包含系统消息和人类消息
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手，你只能输出结构化的json数据\n{format_instructions}"),
        ("human", "请你输出标题为：{topic}的新闻内容"),
    ]
)

# 格式化提示消息，填充主题和格式化指令
prompt = prompt_template.format_messages(
    topic="小米", format_instructions=format_instructions
)

# 记录格式化后的提示消息
logger.info(prompt)

# 调用模型获取结果
result = model.invoke(prompt)

# 记录模型返回的结果
logger.info(f"模型原始输出:\n{result.content}")

# 使用解析器将模型结果解析为Product对象
response = parser.invoke(result)

# 打印解析后的结构化结果
logger.info(f"解析后的结构化结果:\n{response}")

# 打印类型
logger.info(f"结果类型: {type(response)}")
