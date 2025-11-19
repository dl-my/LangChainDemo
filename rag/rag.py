### 文档加载器
"""# Document文档类
from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 1.创建文档加载器，并指定路径
document_load = UnstructuredMarkdownLoader(
    file_path="rag/text/LangChain框架入门09：什么是RAG？.md"
)

# 2.加载文档
documents = document_load.load()

# 3.打印文档内容
print(f"文档数量：{len(documents)}")
for document in documents:
    print(f"文档内容：{document.page_content}")
    print(f"文档元数据：{document.metadata}")"""

# 自定义文档加载器
import os
from datetime import datetime
from langchain_core.documents import Document
from langchain_core.document_loaders.base import BaseLoader


class SimpleQALoader(BaseLoader):
    """
    简单的问答文件加载器

    该加载器用于从文本文件中加载问答对，文件格式要求每两行为一组，
    第一行为问题(Q)，第二行为答案(A)

    Args:
        file_path (str): 问答文件的路径
        time_fmt (str): 时间格式字符串，默认为 "%Y-%m-%d %H:%M:%S"
    """

    def __init__(self, file_path: str, time_fmt: str = "%Y-%m-%d %H:%M:%S"):
        self.file_path = file_path
        self.time_fmt = time_fmt

    def load(self):
        """
        加载并解析问答文件

        读取文件中的问答对，每两行构成一个问答文档，第一行为问题，第二行为答案。
        每个文档包含问题和答案的组合内容，以及文件的元数据信息。

        Returns:
            list[Document]: 包含问答内容的文档列表，每个文档包含page_content和metadata
        """
        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        docs = []
        created_ts = os.path.getctime(self.file_path)
        created_at = datetime.fromtimestamp(created_ts).strftime(self.time_fmt)

        # 每两行构成一个 Q/A
        for i in range(0, len(lines), 2):
            q = lines[i].lstrip("Q：:").strip()
            a = lines[i + 1].lstrip("A：:").strip()
            page_content = f"Q: {q}\nA: {a}"

            doc = Document(
                page_content=page_content,
                metadata={
                    "source": self.file_path,
                    "created_at": created_at,
                },
            )
            docs.append(doc)

        return docs


# if __name__ == "__main__":
#     loader = SimpleQALoader("rag/text/faq.txt")
#     docs = loader.load()
#     print(f"共解析到 {len(docs)} 个文档")
#     for i, d in enumerate(docs, 1):
#         print(f"\n--- 文档 {i} ---")
#         print(d.page_content)
#         print("元数据：", d.metadata)

### 文本分割器
""" # 分割文本
from langchain_text_splitters import RecursiveCharacterTextSplitter

# 1.分割文本内容
content = "大模型RAG（检索增强生成）是一种结合生成模型与外部知识检索的技术，通过从大规模文档或数据库中检索相关信息，辅助生成模型以提升回答的准确性和相关性。其核心流程包括用户输入查询、系统检索相关知识、生成模型基于检索结果生成内容，并输出最终答案。RAG的优势在于能够弥补生成模型的知识盲区，提供更准确、实时和可解释的输出，广泛应用于问答系统、内容生成、客服、教育和企业领域。然而，其也面临依赖高质量知识库、可能的响应延迟、较高的维护成本以及数据隐私等挑战。"
# 2.定义递归文本分割器
# 使用RecursiveCharacterTextSplitter创建文本分割器，设置块大小为100，重叠长度为30
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=30, length_function=len
)

# 3.分割文本
# 将原始文本内容分割成多个文本块
splitter_texts = text_splitter.split_text(content)

# 4.转换为文档对象
# 将分割后的文本块转换为文档对象列表
splitter_documents = text_splitter.create_documents(splitter_texts)
print(f"原始文本大小：{len(content)}")
print(f"分割文档数量：{len(splitter_documents)}")
for splitter_document in splitter_documents:
    print(
        f"文档片段大小：{len(splitter_document.page_content)},文档内容：{splitter_document.page_content}"
    ) """

""" # 分割文档对象
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import UnstructuredFileLoader

# 1.创建文档加载器，进行文档加载
loader = UnstructuredFileLoader("rag/text/rag.txt", encoding="utf-8")
documents = loader.load()

# 2.定义递归文本分割器
# 创建RecursiveCharacterTextSplitter实例，用于将文档分割成指定大小的文本块
# chunk_size: 每个文本块的最大字符数为100
# chunk_overlap: 相邻文本块之间的重叠字符数为30
# length_function: 使用len函数计算文本长度
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=30, length_function=len
)

# 3.分割文本
# 使用文本分割器将加载的文档分割成多个较小的文档片段
splitter_documents = text_splitter.split_documents(documents)

# 输出分割后的文档信息
print(f"分割文档数量：{len(splitter_documents)}")
for splitter_document in splitter_documents:
    print(f"文档片段：{splitter_document.page_content}")
    print(
        f"文档片段大小：{len(splitter_document.page_content)}, 文档元数据：{splitter_document.metadata}"
    ) """

""" # 按标题分割Markdown文件
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import (
    MarkdownHeaderTextSplitter,
    RecursiveCharacterTextSplitter,
)

# 1.文档加载
# 创建文本加载器并加载Markdown文档
loader = TextLoader(file_path="rag/text/solidity.md", encoding="utf-8")
documents = loader.load()
document_text = documents[0].page_content

# 2.定义文本分割器，设置指定要分割的标题
# 配置Markdown标题分割规则，指定不同级别的标题标记及其对应的元数据标签
headers_to_split_on = [("#", "Header 1"), ("##", "Header 2")]
headers_text_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on
)

# 3.按标题分割文档
# 使用标题分割器将文档按Markdown标题结构进行分割
headers_splitter_documents = headers_text_splitter.split_text(document_text)

print(f"按标题分割文档数量：{len(headers_splitter_documents)}")
for splitter_document in headers_splitter_documents:
    print(
        f"按标题分割文档片段大小：{len(splitter_document.page_content)}, 文档元数据：{splitter_document.metadata}"
    )

# 4.定义递归文本分割器
# 创建递归字符分割器，用于进一步细分过大的文档片段
# chunk_size: 每个文本块的目标大小为100个字符
# chunk_overlap: 相邻文本块之间的重叠字符数为30
# length_function: 使用len函数计算文本长度
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100, chunk_overlap=30, length_function=len
)

# 5.递归分割文本
# 对已按标题分割的文档片段进行二次递归分割，确保每个片段不超过指定大小
recursive_documents = text_splitter.split_documents(headers_splitter_documents)
print(f"第二次递归文本分割文档数量：{len(recursive_documents)}")
for recursive_document in recursive_documents:
    print(
        f"第二次递归文本分割文档片段大小：{len(recursive_document.page_content)}, 文档元数据：{recursive_document.metadata}"
    ) """

# 自定义文本分割器
from typing import List

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import TextSplitter


class CustomTextSplitter(TextSplitter):
    """
    自定义文本分割器类

    该类继承自TextSplitter，用于将文本按照特定规则进行分割
    分割策略：首先按段落分割，然后对每个段落提取第一句话
    """

    def split_text(self, text: str) -> List[str]:
        """
        将输入文本分割成多个文本片段

        参数:
            text (str): 需要分割的原始文本字符串

        返回:
            List[str]: 分割后的文本片段列表，每个片段为段落的第一句话
        """
        text = text.strip()
        # 1.按段落进行分割
        text_array = text.split("\n\n")

        result_texts = []
        for text_item in text_array:
            strip_text_item = text_item.strip()
            if strip_text_item is None:
                continue
            # 2.按句进行分割
            result_texts.append(strip_text_item.split("。")[0])
        return result_texts


# 1.文档加载
loader = TextLoader(file_path="rag/text/solidity.md", encoding="utf-8")
documents = loader.load()
document_text = documents[0].page_content

# 2.定义文本分割器
splitter = CustomTextSplitter()

# 3.文本分割
splitter_texts = splitter.split_text(document_text)
for splitter_text in splitter_texts:
    print(f"文本分割片段大小：{len(splitter_text)}, 文本内容：{splitter_text}")
