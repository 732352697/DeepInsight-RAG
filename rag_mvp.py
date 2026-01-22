import os
import sys

# --- 1. 确认身份 (用的是 Python 3.10 吗？) ---
print(f"🐍 当前运行环境: {sys.version.split()[0]}")

# --- 2. 引入 RAG 的核心组件 ---
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate

# 兼容性处理：防止不同版本找不到切分器
try:
    from langchain_text_splitters import CharacterTextSplitter
except ImportError:
    from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain

# --- 3. 配置密钥 (请填入你的 Key) ---
os.environ["OPENAI_API_KEY"] = "f6f8ae4056dc40cd942e8b610af57a62.I3nn1I5xBZLxuLlU"
os.environ["OPENAI_BASE_URL"] = "https://open.bigmodel.cn/api/paas/v4/"

print("\n🚀 RAG 系统正在启动...")

# --- 4. 准备“私有数据” ---
# 这是大模型原本绝对不知道的信息
text_data = """
【未来科技喵喵司员工手册 v1.0】
1. 作息时间：我们实行“睡到自然醒”制度，早上 11:00 前不许到公司，以免打扰前台橘猫睡觉。
2. 福利待遇：每位员工入职即送 500 罐顶级金枪鱼罐头，虽然是给猫吃的，但员工想吃也不拦着。
3. 核心价值观：像猫一样好奇，像狗一样忠诚。
"""

try:
    # --- 5. RAG 四步走 ---

    # 步骤 A: 切分 (Splitting)
    print("1️⃣ 正在切分文档...")
    docs = [Document(page_content=text_data)]
    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=100, chunk_overlap=0)
    split_docs = text_splitter.split_documents(docs)

    # 步骤 B: 向量化与入库 (Indexing)
    print("2️⃣ 正在建立向量数据库 (Chroma)...")
    embeddings = OpenAIEmbeddings(model="embedding-2")  # 智谱的向量模型
    # 建立内存数据库，不存文件，速度快且不报错
    vectorstore = Chroma.from_documents(documents=split_docs, embedding=embeddings)
    print("✅ 向量库构建完成！")

    # 步骤 C: 构建检索链 (Retrieval Chain)
    print("3️⃣ 正在组装 AI 思考链条...")
    llm = ChatOpenAI(model="glm-4", temperature=0)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})  # 只找最相关的一条

    # 告诉 AI：必须根据上下文回答
    prompt = ChatPromptTemplate.from_template("""
    你是一个企业助手。请根据下面的【上下文】来回答用户的问题。
    如果你不知道，就说不知道。

    【上下文】：
    {context}

    用户问题：{input}
    """)

    combine_docs_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    # --- 6. 最终提问 ---
    query = "公司的福利待遇有什么？"
    print(f"\n🙋‍♂️ 用户提问：{query}")

    response = rag_chain.invoke({"input": query})

    print("\n🤖 AI 回答：")
    print("=" * 30)
    print(response["answer"])
    print("=" * 30)

except Exception as e:
    print(f"\n❌ 运行出错: {e}")