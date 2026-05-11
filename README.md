大模型开发
# AIFriends - 大模型AI聊天应用

## 项目概述
AIFriends是一个基于大模型的AI聊天应用，允许用户创建和管理个性化AI角色，并与这些角色进行自然对话。项目采用前后端分离架构，集成了语音合成、长期记忆管理等高级功能，提供沉浸式的AI交互体验。

## 技术栈

### 前端
- **框架**: Vue 3 + Vue Router + Pinia
- **样式**: Tailwind CSS + DaisyUI
- **构建工具**: Vite
- **HTTP客户端**: Axios
- **实时通信**: Server-Sent Events (SSE)
- **其他库**: Highlight.js, Marked, Vditor

### 后端
- **框架**: Django + Django REST Framework
- **认证**: JWT (JSON Web Tokens)
- **AI集成**: LangChain, OpenAI API
- **向量数据库**: LanceDB
- **实时通信**: WebSockets
- **数据库**: SQLite (可扩展为PostgreSQL)

## 核心功能

### 1. 用户认证系统
- 实现了基于JWT的用户认证机制
- 支持用户注册、登录、令牌刷新
- 安全的密码存储和会话管理

### 2. AI角色创建与管理
- 允许用户创建个性化AI角色
- 支持自定义角色名称、头像、背景图片
- 集成语音合成功能，为角色分配独特声音
- 支持角色性格设定和详细描述

### 3. 智能聊天系统
- 基于LangChain构建的对话管理系统
- 流式响应技术，实现实时聊天体验
- 集成OpenAI API，提供高质量对话内容
- 支持上下文理解和多轮对话

### 4. 记忆管理系统
- 实现了AI角色的长期记忆功能
- 每五次对话自动更新角色记忆
- 基于LangChain的记忆检索和更新机制

### 5. 语音交互功能
- 集成语音合成(TTS)功能
- 使用WebSockets实现双向实时语音通信
- 支持语音克隆和自定义语音

## 技术亮点

1. **流式响应技术**: 使用Server-Sent Events (SSE)实现实时聊天体验，提升用户交互感受
2. **AI记忆系统**: 基于LangChain实现的记忆管理，使AI角色能够记住之前的对话内容
3. **语音合成集成**: 通过WebSockets实现实时语音合成，增强交互体验
4. **向量数据库应用**: 使用LanceDB进行向量存储，优化AI响应质量
5. **前后端分离架构**: 清晰的前后端职责划分，便于团队协作和代码维护
6. **安全认证机制**: 基于JWT的安全认证，保障用户数据安全
7. **响应式设计**: 使用Tailwind CSS实现全设备响应式布局

## 项目成果

- 成功实现了一个功能完整的AI聊天应用
- 提供了流畅的用户体验和自然的对话交互
- 展示了大模型技术在实际应用中的落地能力
- 建立了可扩展的架构，为后续功能迭代奠定基础

技术栈：
前端：
Vue3   Tailwind CSS+DaisyUI  Axios  WebRTC VAD   使用Vite构建
后端：
Django  Redis  LangGraph   OpenAI API    Embedding：text-embedding-v4
数据库：
SQLite  与  LanceDB
通信协议：HTTP,SSE,WebSocket,MCP
上线部署:  阿里云服务器，Docker , Nginx,Gunicorn
大模型api:  文字Deepseek   语音阿里云
核心功能：
智能体对话，短期记忆，长期记忆（多轮对话），系统提示词，RAG（实现知识库及查询等功能），ASR，TTS，语音复刻,对话流式 ，构建多个skill工具箱