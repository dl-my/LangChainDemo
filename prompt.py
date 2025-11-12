### 文本提示词模板
#### 创建提示词
"""# 1 使用构造方法
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象,用于生成格式化的提示词模板
# 该模板包含两个变量: role(角色)和question(问题)
template = PromptTemplate(
    template="你是一个专业的{role}工程师,请对我的问题给出回答,我的问题是: {question}",
    input_variables=["role", "question"],
)

# 使用模板格式化具体的提示词内容
# 将role替换为"python开发",question替换为"冒泡排序怎么写？"
prompt = template.format(role="python开发", question="冒泡排序怎么写?")
print(prompt)"""

""" # 2 调用from_template(常用)
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象,用于生成格式化的提示词模板
# 模板包含两个占位符: {role}表示角色,{question}表示问题
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师,请对我的问题给出回答,我的问题是: {question}"
)

# 使用指定的角色和问题参数来格式化模板,生成最终的提示词字符串
# role: 工程师角色描述
# question: 具体的技术问题
prompt = template.format(role="python开发", question="冒泡排序怎么写?")
print(prompt) """

""" # 3 部分提示词模板
from datetime import datetime
from langchain_core.prompts import PromptTemplate

# 创建一个包含时间变量的模板,时间变量使用partial_variables预设为当前时间
# 然后格式化问题生成最终提示词
template1 = PromptTemplate.from_template(
    "现在时间是:{time},请对我的问题给出答案,我的问题是:{question}",
    partial_variables={"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")},
)

prompt1 = template1.format(question="今天是几号?")
print(prompt1)

# 创建一个包含时间变量的模板,通过partial方法预设时间变量为当前时间
# 然后格式化问题生成最终提示词
template2 = PromptTemplate.from_template(
    "现在时间是:{time},请对我的问题给出答案,我的问题是:{question}"
)
partial = template2.partial(time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
prompt2 = partial.format(question="今天是几号?")
print(prompt2) """

""" # 4 组合提示词模板
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate模板,用于生成介绍某个主题的提示词
# 该模板包含两个占位符: topic(主题)和length(字数限制)
template1 = (
    PromptTemplate.from_template("请用一句话介绍{topic},要求通俗易懂\n")
    + "内容不超过{length}个字"
)

# 使用format方法填充模板中的占位符,生成具体的提示词
prompt1 = template1.format(topic="LangChain", length=20)
print(prompt1)

# 分别创建两个独立的PromptTemplate模板
template_a = PromptTemplate.from_template("请用一句话介绍{topic},要求通俗易懂\n")
template_b = PromptTemplate.from_template("内容不超过{length}个字")
# 将两个模板进行拼接组合
template_all = template_a + template_b
# 填充组合后模板的占位符,生成最终的提示词
prompt2 = template_all.format(topic="LangChain", length=20)
print(prompt2) """

#### 提示词方法 format(),partial(),invoke()
""" # format() 将question参数格式化到提示词模板中,返回一个字符串
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象,用于生成格式化的提示词模板
# 模板包含两个占位符: {role}表示角色,{question}表示问题
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师,请回答我的问题给出回答,我的问题是: {question}"
)

# 使用指定的角色和问题参数来格式化模板,生成最终的提示词字符串
prompt = template.format(role="python开发", question="冒泡排序怎么写？")

# 输出生成的提示词
print(prompt)
print(type(prompt)) """

""" # partial() 可以格式化部分变量,并且继续返回一个模板,通常在部分提示词模板场景下使用
from langchain_core.prompts import PromptTemplate

# 创建模板对象,定义提示词模板格式
# 模板包含两个占位符: role(角色)和 question(问题)
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师,请回答我的问题给出回答,我的问题是: {question}"
)

# 使用partial方法固定role参数为"python开发"
# 返回一个新的模板对象,其中role参数已被绑定
partial = template.partial(role="python开发")

# 打印partial对象及其类型信息
print(partial)
print(type(partial))

# 使用format方法填充question参数,生成最终的提示词字符串
# 此时所有占位符都已填充完毕,返回完整的提示词文本
prompt = partial.format(question="冒泡排序怎么写？")

# 输出生成的提示词
print(prompt)
print(type(prompt)) """

""" # invoke() 是LangChainExpressionLanguage(LCEL的统一执行入口,用于执行任意可运行对象(Runnable)。返回的是一个 PromptValue 对象,可以用 .to_string()或 .to_messages()查看内容
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象,用于生成格式化的提示词模板
# 模板中包含两个占位符: {role}表示角色,{question}表示问题
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师,请回答我的问题给出回答,我的问题是: {question}"
)

# 使用invoke方法填充模板中的占位符,生成具体的提示词
# 参数: 字典类型,包含role和question两个键值对
# 返回值: PromptValue对象,包含了格式化后的提示词
prompt = template.invoke({"role": "python开发", "question": "冒泡排序怎么写？"})

# 打印PromptValue对象及其类型
print(prompt)
print(type(prompt))

# 将PromptValue对象转换为字符串并打印
# to_string()方法将PromptValue转换为可读的字符串格式
print(prompt.to_string())
print(type(prompt.to_string())) """


### 对话提示词模板
#### 创建提示词
""" # 1 使用构造方法
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，包含系统角色设定、用户询问和AI回答的对话历史
# 以及用户当前输入的占位符
prompt_template = ChatPromptTemplate(
    [
        ("system", "你是一个AI助手, 你的名字是{name}"),
        ("human", "你能做什么事"),
        ("ai", "我可以陪你聊天，讲笑话，写代码"),
        ("human", "{user_input}"),
    ]
)

# 使用指定的参数格式化提示模板，生成最终的提示字符串
# name: AI助手的名称
# user_input: 用户的当前输入
prompt = prompt_template.format(name="小张", user_input="你可以做什么")
print(prompt) """

""" # 2 调用form_message(常用)
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，包含系统角色设定和用户问题格式
# 系统消息定义了AI的角色,人类消息定义了问题的输入格式
chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个{role}，请回答我提出的问题"), ("human", "请回答:{question}")]
)

# 使用指定的角色和问题参数填充模板，生成具体的提示内容
prompt_value = chat_prompt.invoke(
    {"role": "python开发工程师", "question": "冒泡排序怎么写"}
)

# 输出生成的提示内容
print(prompt_value.to_string()) """

#### 提示词方法 format_messages(),format_prompt()
""" # format_messages() 将模板变量替换后，直接生成 消息列表(List[BaseMessage]),一般包含: SystemMessage``HumanMessage``AIMessage
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，包含系统角色设定和用户问题格式
# 系统消息定义了AI助手的角色，人类消息定义了用户问题的格式
chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个{role}，请回答我提出的问题"), ("human", "请回答:{question}")]
)

# 格式化聊天提示模板，填充角色和问题参数
# 参数role: 指定AI助手的角色身份
# 参数question: 用户提出的具体问题
# 返回值: 格式化后的消息列表
prompt_value = chat_prompt.format_messages(
    role="python开发工程师", question="冒泡排序怎么写"
)

# 打印格式化后的提示消息
print(prompt_value) """

""" # format_prompt() 生成一个 PromptValue 对象,这是一种抽象层次更高的封装
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，包含系统角色设定和用户问题格式
# 该模板定义了两个消息：系统消息用于设定AI助手的角色，人类消息用于接收用户的具体问题
chat_prompt = ChatPromptTemplate.from_messages(
    [("system", "你是一个{role}，请回答我提出的问题"), ("human", "请回答:{question}")]
)

# 使用指定的角色和问题参数格式化聊天提示模板
# role: 指定AI助手的角色身份
# question: 用户提出的具体问题
# 返回格式化后的提示对象，可用于后续的模型调用
prompt = chat_prompt.format_prompt(role="python开发工程师", question="冒泡排序怎么写")

# 打印格式化后的提示内容
print(prompt)

# 将提示转换为消息列表并打印
print(prompt.to_messages()) """

#### 实例化参数类型
""" # str类型 （不推荐），因为默认都是HumanMessage。
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，用于构建AI助手的对话上下文
# 该模板包含两个消息：AI助手的自我介绍和用户问题
chat_prompt = ChatPromptTemplate.from_messages(
    ["你是AI助手,你的名字叫{name}", "请问: {question}"]
)

# 格式化聊天提示模板，填充具体的助手名称和问题内容
# 参数name: AI助手的名字
# 参数question: 用户提出的问题
# 返回值: 格式化后的消息列表
message = chat_prompt.format_messages(name="亮仔", question="什么是LangChain")

print(message) """

""" # dict 类型
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，用于构建AI助手的对话上下文
# 该模板包含两个消息：AI助手的自我介绍和用户问题
chat_prompt = ChatPromptTemplate.from_messages(
    [
        {"role": "system", "content": "你是AI助手,你的名字叫{name}"},
        {"role": "user", "content": "请问:{question}"},
    ]
)

# 格式化聊天提示模板，填充具体的助手名称和问题内容
# 参数name: AI助手的名字
# 参数question: 用户提出的问题
# 返回值: 格式化后的消息列表
message = chat_prompt.format_messages(name="亮仔", question="什么是LangChain")

print(message) """

""" # message 类型
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，用于构建AI助手的对话上下文
# 该模板包含两个消息：AI助手的自我介绍和用户问题
chat_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="你是AI助手，你的名字叫{name}。"),
        HumanMessage(content="请问：{question}"),
    ]
)

# 格式化聊天提示模板，填充具体的助手名称和问题内容
# 参数name: AI助手的名字
# 参数question: 用户提出的问题
# 返回值: 格式化后的消息列表
message = chat_prompt.format_messages(name="亮仔", question="什么是LangChain")

print(message) """

""" # BaseChatPromptTemplate 类型
from langchain_core.prompts import ChatPromptTemplate

# 创建系统消息模板，用于定义AI助手的身份信息
prompt_template1 = ChatPromptTemplate.from_messages(
    [("system", "你是AI助手，你的名字叫{name}。")]
)

# 创建人类消息模板，用于定义用户提问的格式
prompt_template2 = ChatPromptTemplate.from_messages([("human", "请问：{question}")])

# 将系统消息模板和人类消息模板组合成完整的对话模板
chat_prompt = ChatPromptTemplate.from_messages([prompt_template1, prompt_template2])

# 使用指定的参数格式化消息模板，生成实际的消息内容
message = chat_prompt.format_messages(name="亮仔", question="什么是LangChain")

print(message) """

""" # BaseMessagePromptTemplate 类型
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# 创建系统消息模板，用于定义AI助手的身份信息
system_prompt = SystemMessagePromptTemplate.from_template(
    "你是AI助手，你的名字叫{name}。"
)

# 创建人类消息模板，用于定义用户提问的格式
human_prompt = HumanMessagePromptTemplate.from_template("请回答：{question}")

# 创建具体的系统消息和人类消息实例
system_msg = SystemMessage(content="你是AI工程师")
human_msg = HumanMessage(content="你好")

# 创建嵌套的消息模板，包含预定义的系统和人类消息
nested_prompt = ChatPromptTemplate.from_messages([system_msg, human_msg])

# 构建完整的聊天提示模板，组合了模板和具体消息
chat_prompt = ChatPromptTemplate.from_messages(
    [system_prompt, human_prompt, system_msg, human_msg, nested_prompt]
)

# 格式化消息并打印结果
message = chat_prompt.format_messages(name="亮仔", question="什么是LangChain")
print(message) """


### 少量样本提示词模板
""" # FewShotPromptTemplate
from langchain_core.prompts import FewShotPromptTemplate, PromptTemplate

# 几个示例，说明模型该如何输出
examples = [
    {"input": "北京下雨吗", "output": "北京"},
    {"input": "上海热吗", "output": "上海"},
]

# 定义如何格式化每个示例
example_prompt = PromptTemplate(
    input_variables=["input", "output"], template="输入:{input}\n输出:{output}"
)

# 构建 FewShotPromptTemplate
few_shot_prompt = FewShotPromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
    prefix="按提示的格式,输出内容",
    suffix="输入:{input}\n输出:",  # 要放在示例后面的提示模板字符串。
    input_variables=["input"],  # 传入的变量
)

# 生成最终的 prompt
print(few_shot_prompt.format(input="天津今天刮风吗")) """

""" # FewShotChatMessagePromptTemplate
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate

# 定义示例数据，用于少样本学习
# 包含输入输出对，展示乘法运算的格式和结果
examples = [{"input": "1×2", "output": "2"}, {"input": "2×2", "output": "4"}]

# 创建示例提示模板，定义了人类提问和AI回答的交互格式
# human消息使用"{input}是多少"的模板
# ai消息使用"{output}"的模板
example_prompt = ChatPromptTemplate.from_messages(
    [("human", "{input}是多少"), ("ai", "{output}")]
)

# 创建少样本聊天消息提示模板
# 使用预定义的示例数据和示例提示模板
# 该模板将用于在最终提示中提供上下文示例
few_shot_prompt = FewShotChatMessagePromptTemplate(
    examples=examples,
    example_prompt=example_prompt,
)

# 构建最终的提示模板
# 组合系统角色设定、少样本示例和用户问题
# 系统设定AI为数学奇才，然后添加示例，最后是用户的具体问题
final_prompt = (
    ChatPromptTemplate.from_messages([("system", "你是一名百年一遇的数学奇才")])
    + few_shot_prompt
    + ChatPromptTemplate.from_messages([("human", "{question}")])
)

# 格式化并打印最终提示模板，传入具体问题"3✖️2"
print(final_prompt.format(question="3×2")) """
