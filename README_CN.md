![cover-v5-optimized](/assets/readme_cover.png)

<p align="center">
  📌 <a href="https://easydoc.sh/">介绍 Easydoc API：强大的多模态文档处理 API</a>
</p>

<p align="center">
  <a href="https://platform.easydoc-ai.sh">Easydoc API Platform</a> 
  <!-- ·
   <a href="https://easydoc-ai.sh">文档</a> -->
</p>

<p align="center">
    <a href="https://easydoc.sh" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/product-F04438"></a>
    <a href="https://discord.gg/kMgjbHxm" target="_blank">
        <img src="https://img.shields.io/discord/1319201673201324032?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="Discord 聊天"></a>
    <a href="https://twitter.com/intent/follow?screen_name=EasyDoc_AI" target="_blank">
        <img src="https://img.shields.io/twitter/follow/EasyDoc_AI?logo=X&color=%20%23f5f5f5"
            alt="关注 X (Twitter)"></a>
    <a href="https://github.com/easydoc-ai/easydoc" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3Aeasydoc-ai%2Feasydoc%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://github.com/easydoc-ai/easydoc/discussions/" target="_blank">
        <img alt="讨论帖子" src="https://img.shields.io/github/discussions/easydoc-ai/easydoc?labelColor=%20%239b8afb&color=%20%237a5af8"></a>
</p>

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README_CN.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
</p>

## 💡 什么是 EasyDoc？

EasyDoc 是一个强大的多模态文档处理 API，能够将非结构化文档转换为结构化的分层 JSON，使文档资产完美适用于您的 AI 和 LLM 应用。专为 LLM 管道设计，EasyDoc 为模型推理、微调和优化的上下文窗口提供高质量的数据。

### 为什么选择 EasyDoc？

- 📄 智能布局分析：

    自动将文档解析为分层 JSON，保留逻辑结构、章节关系和阅读顺序。非常适合通过优化的上下文窗口最大化 LLM 性能。
- 🔍 丰富的语义提取：

    准确提取标题、章节、段落和列表等元数据，生成创意思维导图和具有完整层次关系的结构化 JSON 输出，用于细粒度导航和 LLM 上下文增强。
- 🎨 多模态内容解析：

    将表格、图表和视觉元素无缝转换为结构化 JSON，保持与周围文本的上下文关系。完全兼容 LLM 管道，以提升性能。

## 🚀 快速开始

- 获取 API 密钥

  要开始使用 Easydoc API，您首先需要生成一个 API 密钥。请按照以下步骤操作：

  1. **访问 API 密钥管理页面**：
     在浏览器中访问 [Easydoc API 密钥](https://platform.easydoc.sh/api-keys)。
  2. **登录**：
     如果尚未登录，请使用您的凭据登录 Easydoc 账户。
  3. **生成新的 API 密钥**：
     登录后，您可以创建一个新的 API 密钥。点击“创建新密钥”按钮。
  4. **复制您的 API 密钥**：
     密钥生成后，将显示一个唯一的 API 密钥。将其复制到剪贴板。
  5. **使用 API 密钥**：
     您现在可以使用此 API 密钥在与 Easydoc API 交互时进行身份验证。

  请确保妥善保管您的 API 密钥，不要将其暴露在公共仓库或未经授权的地方。

- 使用 REST API

  您可以使用以下两个端点与 Easydoc API 进行交互：

   #### 1. **POST api/v1/parse**  
   此 API 允许您上传文件并创建解析任务。

   **操作步骤**：
   - **发送 POST 请求**到 `api/v1/parse`，并在请求体中上传您希望解析的文件。
   - **响应**：服务器将返回一个 `task_id`，您可以使用它来跟踪解析任务的状态。

   有关详细的 API 文档和使用说明，请查看 [POST /api/v1/parse 的 API 参考](/docs/api-reference/parse.md)。

   ---

   #### 2. **GET api/v1/parse/{task_id}/result**  
   此 API 允许您检索之前创建的解析任务的结果。

   **操作步骤**：
   - **发送 GET 请求**到 `api/v1/parse/{task_id}/result`，将 `{task_id}` 替换为上一步返回的任务 ID。
   - **响应**：任务完成后，您将收到解析结果。

   有关如何使用此端点的更多详细信息，请访问 [GET /api/v1/parse/{task_id}/result 的 API 参考](/docs/api-reference/parse_result.md)。

   --- 

## 💰 定价

| 计划           | 价格           | 免费试用  | 备注                                           |
|----------------|----------------|-------------|------------------------------------------------|
| Lite           | $2/1000 页  | 1000 页  | 基本功能                                 |
| Pro            | $8/1000 页  | 1000 页  | 高级功能                              |
| Premium (Beta) | 联系我们      | 500 页   | 试用版的前沿功能，需要 API 密钥 |

## 💬 支持与反馈

- Discord: 加入我们的 Discord 社区 [Room Url](https://discord.gg/kMgjbHxm)
- 邮箱: 联系邮箱
- 服务条款: 链接
- 隐私政策: 链接
```