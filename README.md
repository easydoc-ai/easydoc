![cover-v5-optimized](/assets/readme_cover.png)

<p align="center">
  📌 <a href="https://easydoc.sh/">Introducing EasyDoc API: Powerful Multimodal Document Processing API</a>
</p>



<p align="center">
  <a href="https://platform.easydoc-ai.sh">EasyDoc API Platform</a> 
  <!-- ·
   <a href="https://easydoc-ai.sh">Documentation</a> -->
</p>

<p align="center">
    <a href="https://easydoc.sh" target="_blank">
        <img alt="Static Badge" src="https://img.shields.io/badge/product-F04438"></a>
    <a href="https://discord.gg/jRSkyCeN" target="_blank">
        <img src="https://img.shields.io/discord/1319201673201324032?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
            alt="chat on Discord"></a>
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

EasyDoc is a powerful multimodal document processing API that transforms unstructured documents into hierarchical JSON, making document assets perfect for your AI and LLM applications. Purpose-built for LLM pipelines, EasyDoc provides high-quality data for model inference, fine-tuning, and optimized context windows.

### Why Choose EasyDoc?

- 🧩 Content Block Identification:

    Transform scattered document text into meaningful knowledge blocks, moving far beyond simple line-by-line parsing. Our AI precisely identifies and groups related content, creating optimized context windows perfect for LLM consumption.

- 🔍 Rich Semantic Extraction:

    Automatically reconstruct document hierarchies into intuitive mind maps, providing LLMs with rich context. Our deep understanding of document organization ensures your AI models receive complete, well-organized information for better reasoning and responses.
  
- 🎨 Multimodal Content Parsing:

    Convert complex tables, figures, and visual data into JSON that your AI can actually understand. From multi-level tables to intricate diagrams, EasyDoc transforms multimodal content into machine-readable knowledge, supercharging your AI applications' capabilities.


## 🚀 Getting Started

- Get an API key

  To get started with the EasyDoc API, you'll first need to generate an API key. Follow these steps:

  1. **Visit the API Key Management Page**:
     Go to [EasyDoc API Keys](https://platform.easydoc.sh/api-keys) in your browser.
  2. **Log In**:
     If you aren't already logged in, sign in to your EasyDoc account using your credentials.
  3. **Generate a New API Key**:
     Once logged in, you will be able to create a new API key. Click on the "Create New Key" button.
  4. **Copy Your API Key**:
     After the key is generated, a unique API key will be displayed. Copy the key to your clipboard.
  5. **Use the API Key**:
     You can now use this API key to authenticate your requests when interacting with the EasyDoc API.

  Make sure to keep your API key secure and do not expose it in public repositories or unauthorized places.

- Use the REST API
  
  You can interact with the EasyDoc API using the following two endpoints:

   #### 1. **POST api/v1/parse**  
   This API allows you to upload a file and create a parsing task. 

   **Operation Steps**:
   - **Send a POST request** to `api/v1/parse` with the file you wish to upload in the request body.
   - **Response**: The server will return a `task_id` that you can use to track the status of the parsing task.

   For detailed API documentation and usage instructions, check the [API Reference for POST /api/v1/parse](/docs/api-reference/parse.md).

   ---

   #### 2. **GET api/v1/parse/{task_id}/result**  
   This API allows you to retrieve the result of the parsing task you previously created.

   **Operation Steps**:
   - **Send a GET request** to `api/v1/parse/{task_id}/result`, replacing  `{task_id}` with the task ID returned from the previous step.
   - **Response**: You will receive the parsing result once the task is complete.

   For more details on how to use this endpoint, visit the [API Reference for GET /api/v1/parse/{task_id}/result](/docs/api-reference/parse_result.md).

   --- 

## 💰 Pricing

| Plan           | Price           | Free Trial  | Notes                                           |
|----------------|-----------------|-------------|------------------------------------------------|
| Lite           | $2/1000 pages  | 1000 pages  | Basic features                                 |
| Pro            | $8/1000 pages  | 1000 pages  | Advanced features                              |
| Premium (Beta) | N/A            | 500 pages   | Cutting-edge features for trials, [join waitlist](https://easydoc.sh/join-waitlist) to get your API key. |


## 💬 Support and Feedback
- Join our [Discord](https://discord.gg/jRSkyCeN) community for support 
- Contact us at cooperate@easylink-ai.com
- [Terms of Service](https://easydoc.sh/terms)
- [Privacy Policy](https://easydoc.sh/privacy)

Ready to try? Sign up for free and get 1000 pages to test!
