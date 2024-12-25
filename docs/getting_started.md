### Getting Started

#### Overview

- Easydoc API 的功能与适用场景简介。
- 主要优势与核心特点。

#### Quick starts

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


