![cover-v5-optimized](/assets/readme_cover.png)

<p align="center">
  📌 <a href="https://easydoc.sh/">Introducing Easydoc Api: Powerful Multimodal Document Processing API</a>
</p>



<p align="center">
  <a href="https://platform.easydoc-ai.sh">Easydoc API Platform</a> 
  <!-- ·
   <a href="https://easydoc-ai.sh">Documentation</a> -->
</p>

<p align="center">
    <a href="https://easydoc.sh" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/product-F04438"></a>
    <a href="https://easydoc.sh/pricing" target="_blank">
        <img alt="Static Badge" src="
        https://img.shields.io/badge/pricing-%20%23155EEF
        "></a>
    <a href="https://discord.gg/kMgjbHxm" target="_blank">
        <img src="https://img.shields.io/discord/1319201673201324032?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
    <a href="https://reddit.com/r/Easydocai" target="_blank">  
        <img src="https://img.shields.io/reddit/subreddit-subscribers/Easydocai?style=plastic&logo=reddit&label=r%2FEasydocai&labelColor=white"
            alt="join Reddit"></a>
    <a href="https://twitter.com/intent/follow?screen_name=EasyDoc_AI" target="_blank">
        <img src="https://img.shields.io/twitter/follow/EasyDoc_AI?logo=X&color=%20%23f5f5f5"
            alt="follow on X(Twitter)"></a>
    <a href="https://github.com/easydoc-ai/easydoc" target="_blank">
        <img alt="Issues closed" src="https://img.shields.io/github/issues-search?query=repo%3Aeasydoc-ai%2Feasydoc%20is%3Aclosed&label=issues%20closed&labelColor=%20%237d89b0&color=%20%235d6b98"></a>
    <a href="https://github.com/easydoc-ai/easydoc/discussions/" target="_blank">
        <img alt="Discussion posts" src="https://img.shields.io/github/discussions/easydoc-ai/easydoc?labelColor=%20%239b8afb&color=%20%237a5af8"></a>
</p>

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="./README_CN.md"><img alt="简体中文版自述文件" src="https://img.shields.io/badge/简体中文-d9d9d9"></a>
</p>

## 💡 What is EasyDoc?

EasyDoc is a powerful multimodal document processing API that transforms unstructured documents into structured, hierarchical JSON, making document assets perfect for your AI and LLM applications. Purpose-built for LLM pipelines, EasyDoc provides high-quality data for model inference, fine-tuning, and optimized context windows.

### Why Choose EasyDoc?

- 📄 Intelligent Layout Analysis:

    Automatically parse documents into hierarchical JSON, preserving the logical structure, section relationships, and reading order. Perfect for maximizing LLM performance with optimized context windows.
- 🔍 Rich Semantic Extraction:

    Accurately extract metadata such as titles, sections, paragraphs, and lists, generating a creative mind map and structured JSON outputs with full hierarchical relationships for fine-grained navigation and LLM context enrichment.
- 🎨 Multimodal Content Parsing:

    Seamlessly transform tables, figures, and visual elements into structured JSON, maintaining contextual relationships with surrounding text. Fully compatible with LLM pipelines for enhanced performance.


## 🚀 Getting Started

- Get an API key

  To get started with the Easydoc API, you'll first need to generate an API key. Follow these steps:

  1. **Visit the API Key Management Page**:
     Go to [Easydoc API Keys](https://platform.easydoc.sh/api-keys) in your browser.
  2. **Log In**:
     If you aren't already logged in, sign in to your Easydoc account using your credentials.
  3. **Generate a New API Key**:
     Once logged in, you will be able to create a new API key. Click on the "Create New Key" button.
  4. **Copy Your API Key**:
     After the key is generated, a unique API key will be displayed. Copy the key to your clipboard.
  5. **Use the API Key**:
     You can now use this API key to authenticate your requests when interacting with the Easydoc API.

  Make sure to keep your API key secure and do not expose it in public repositories or unauthorized places.

- Use the REST API
  Sure! Here's the content for the "Use the REST API" section:

  You can interact with the Easydoc API using the following two endpoints:

   #### 1. **POST api/v1/parse**  
   This API allows you to upload a file and create a parsing task. 

   **Operation Steps**:
   - **Send a POST request** to `api/v1/parse` with the file you wish to   upload in the request body.
   - **Response**: The server will return a `task_id` that you can use to  track the status of the parsing task.

   For detailed API documentation and usage instructions, check the [API Reference for POST /api/v1/parse](/docs/api-reference/parse.md).

   ---

   #### 2. **GET api/v1/parse/{task_id}/result**  
   This API allows you to retrieve the result of the parsing task you   previously created.

   **Operation Steps**:
   - **Send a GET request** to `api/v1/parse/{task_id}/result`, replacing  `{task_id}` with the task ID returned from the previous step.
   - **Response**: You will receive the parsing result once the task is    complete.

   For more details on how to use this endpoint, visit the [API Reference for GET /api/v1/parse/{task_id}/result](/docs/api-reference/parse_result.md).

   --- 

## 💰 Pricing

| Plan           | Price           | Free Trial  | Notes                                           |
|----------------|-----------------|-------------|------------------------------------------------|
| Lite           | $2/1000 pages  | 1000 pages  | Basic features                                 |
| Pro            | $8/1000 pages  | 1000 pages  | Advanced features                              |
| Premium (Beta) | Contact us      | 500 pages   | Cutting-edge features for trials, requires API key |


## 💬 Support and Feedback

- Discord: Join our Discord community  [Room Url](https://discord.gg/kMgjbHxm)
- Email: Contact email
- Terms of Service:  Link
- Privacy Policy:  Link
