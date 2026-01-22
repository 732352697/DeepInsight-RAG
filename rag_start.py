import os
import sys
from langchain_openai import ChatOpenAI

# --- 0. 确认我们在用 Python 3.10 ---
print(f"🐍 当前 Python 版本: {sys.version.split()[0]}")
# 这里的路径应该是 C:\Users\Chen\...\Python310\python.exe
print(f"📂 当前解释器路径: {sys.executable}")

# --- 1. 配置 Key ---
# ⚠️⚠️⚠️ 请把下面引号里的内容换成你的 Key ⚠️⚠️⚠️
os.environ["OPENAI_API_KEY"] = "f6f8ae4056dc40cd942e8b610af57a62.I3nn1I5xBZLxuLlU"
os.environ["OPENAI_BASE_URL"] = "https://open.bigmodel.cn/api/paas/v4/"

print("\n🚀 正在测试连接...")

try:
    # --- 2. 简单测试 ---
    llm = ChatOpenAI(
        model="glm-4",
        temperature=0.1
    )

    print("⏳ 正在发送请求给智谱AI...")
    response = llm.invoke("你好，如果你能听到我说话，请回复'连接成功'这四个字")

    print("\n" + "=" * 20)
    print(f"🤖 模型回复: {response.content}")
    print("=" * 20 + "\n")
    print("✅ 恭喜！环境配置成功，我们可以开始写 RAG 了！")

except Exception as e:
    print(f"\n❌ 连接失败: {e}")