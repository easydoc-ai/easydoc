![cover-v5-optimized](/assets/readme_cover.png)

<p align="center">
  📌 <a href="https://easydoc.sh/">EasyDoc：强大的多模态文档处理 API</a>
</p>

<p align="center">
  <a href="https://platform.easydoc-ai.sh">EasyDoc API Platform</a> 
  <!-- ·
   <a href="https://easydoc-ai.sh">文档</a> -->
</p>

<p align="center">
    <a href="https://easydoc.sh" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/product-F04438"></a>
    <a href="https://discord.gg/jRSkyCeN" target="_blank">
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

EasyDoc 是一款强大的多模态文档处理 API，能够精准解读文本和图表中的层次结构与逻辑关系，将非结构化文档转化为 JSON 格式数据，为大语言模型（LLM）应用提供全面而丰富的上下文信息，同时为 LLM 的推理与训练提供高质量数据支持。

### 为什么选择 EasyDoc？

- 📄 智能布局分析：

    超越传统的行文分割方法，自动解析文档内容，重组零散文本为大语言模型（LLM）可理解的语义知识块。精准梳理文档逻辑关系，为 LLM 提供更具深度的结构化语义支持。
- 🔍 丰富的语义提取：

    智能识别文档的整体结构，提取标题、章节、段落及列表等核心元数据，构建具有层次关系的文档结构树。帮助 LLM 注入完整的上下文认知，用于上下文增强、导航和语义推理。
- 🎨 多模态内容解析：

    对复杂表格、图表及视觉元素进行深度语义解析，精准还原其与文本上下文的关联，全面提升 LLM 与多模态 AI 在推理和应用中的表现。
## 🚀 快速开始

### 1. 获取 API 密钥

  要开始使用 EasydDoc API，您首先需要生成一个 API 密钥。请按照以下步骤操作：

  1. **访问 API 密钥管理页面**：
     在浏览器中访问 [EasyDoc API 密钥](https://platform.easydoc.sh/api-keys)。
  2. **登录**：
     如果尚未登录，请使用您的凭据登录 EasyDoc 账户。
  3. **生成新的 API 密钥**：
     登录后，您可以创建一个新的 API 密钥。点击“创建新密钥”按钮。
  4. **复制您的 API 密钥**：
     密钥生成后，将显示一个唯一的 API 密钥。将其复制到剪贴板。
  5. **使用 API 密钥**：
     您现在可以使用此 API 密钥在与 EasyDoc API 交互时进行身份验证。

  请确保妥善保管您的 API 密钥，不要将其暴露在公共仓库或未经授权的地方。

### 2. 使用 REST API

  您可以使用以下两个端点与 EasyDoc API 进行交互：

   #### 1. **POST api/v1/parse**  
   此 API 允许您上传文件并创建解析任务。
> **实用提示：**  
> - **支持的文件类型**：请确保上传的文件属于以下格式之一：  
>   - PDF 文件（.pdf）  
>   - 文本文件（.txt）  
>   - Word 文档（.docx, .doc）  
>   - PowerPoint 演示文稿（.pptx, .ppt）  
> - **文件大小限制**：每个文件的最大支持大小为 100 MB。请确保上传的文件不超过此限制，以避免请求失败。
  
   - **发送 POST 请求**到 `api/v1/parse`，将您需要上传的文件包含在请求体中。同时，将 `api-key` 替换为您的个人 API 密钥。为了获得最快的处理速度，我们建议从 `lite` 模式开始。

  ``` shell
      curl https://api.easydoc.sh/api/v1/parse \
	-X POST \
	-H "api-key: your-api-key" \
	-F "file=@demo_document.pdf" \
	-F "mode=lite" \
  ``` 
  

   - **响应**：你将在服务响应中收到一个 `task_id`，接下来可以使用它来跟踪解析任务的状态。
  

   有关详细的 API 文档和使用说明，请查看 [POST /api/v1/parse 的 API 参考](/docs/api-reference/parse.md)。

   ---

   #### 2. **GET api/v1/parse/{task_id}/result**  
   此 API 允许您检索之前创建的解析任务的结果。

   **操作步骤**：
   - **发送 GET 请求**到 `api/v1/parse/{task_id}/result`，将 `{task_id}` 替换为上一步返回的任务 ID。
   ``` bash
   curl "https://api.easydoc.sh/api/v1/parse/{task_id}/result"  \
    -X GET \
	-H "api-key: your-api-key"
   ```
   - **响应**：任务完成后，您将收到解析结果。

   有关如何使用此端点的更多详细信息，请访问 [GET /api/v1/parse/{task_id}/result 的 API 参考](/docs/api-reference/parse_result.md)。

   --- 

## 💰 定价
🎉 新用户福利：立享$10免费额度

| 计划           | 价格           | 免费试用  | 备注                                           |
|----------------|----------------|-------------|------------------------------------------------|
| Lite           | $2/1000 页  | 1000 页  | 基本功能                                 |
| Pro            | $8/1000 页  | 1000 页  | 高级功能                              |
| Premium (Beta) | 免费        | 500 页   | 试用版的前沿功能，[预约优先体验](https://easydoc.sh/zh/join-waitlist)获得API密钥    |

## 💬 支持与反馈

扫二维码添加进 EasyDoc 交流群，交流内测反馈。

![EasyDoc交流群](https://github.com/user-attachments/assets/da4a5342-ab73-425d-987f-a87d96644d74)

