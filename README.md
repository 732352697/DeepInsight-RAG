# 🧠 DeepInsight: Enterprise-Grade Private RAG System

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/Framework-LangChain-green)
![Ollama](https://img.shields.io/badge/LLM-Ollama-orange)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)

> **DeepInsight** 是一个基于 **Ollama + LangChain** 架构的私有化文档问答系统。它专为对数据隐私有高要求的企业环境设计，支持在纯 CPU 环境下离线运行，并实现了类似 DeepSeek 的“深度思考”流式交互体验。

## ✨ 核心亮点 (Key Features)

* **🔒 100% 数据私有化**: 全链路本地运行（Localhost），无需调用 OpenAI API，确保敏感数据不出域。
* **📂 全能文档解析 (ETL)**: 支持 **PDF, Word, Excel, PPT** 多格式混合上传与解析，自动清洗非结构化数据。
* **🧠 深度思考 UI (Chain-of-Thought)**: 实现了仿 DeepSeek 的思维链可视化组件，实时展示“检索-规划-生成”的全过程。
* **⚡ 极致性能优化**:
    * **流式响应 (Streaming)**: 将首字延迟 (TTFT) 降低至 0.5s 内。
    * **防崩溃机制**: 实现了 Streamlit 渲染频率控制（Time Throttling），解决了高频 Token 生成导致的前端崩溃问题。
    * **轻量化模型**: 适配 Qwen2.5-1.5B 模型，在普通办公本上即可流畅运行。

## 🛠️ 技术栈 (Tech Stack)

* **LLM Runtime**: [Ollama](https://ollama.com/) (Running Qwen2.5-1.5B)
* **Orchestration**: LangChain (Community & Ollama libs)
* **Frontend**: Streamlit (with Custom CSS & Session State management)
* **Document Loaders**: PyPDF, python-docx, openpyxl, python-pptx

## 🚀 快速开始 (Quick Start)

### 1. 环境准备
确保你已经安装了 Python 3.10+ 和 [Ollama](https://ollama.com/)。

### 2. 下载模型
在终端运行以下命令，拉取适配的轻量化模型：
```bash
ollama pull qwen2.5:1.5b