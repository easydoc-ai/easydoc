

## 🚀 Getting Started

### 1. Get an API key

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

### 2. Use the REST API
  
  You can interact with the EasyDoc API using the following two endpoints:

   #### 1. **POST api/v1/parse**  
   This API allows you to upload a file and create a parsing task. 
  > Useful tips:
  >* Supported file types: Ensure the uploaded file is in one of the following formats:
  >    * PDF (.pdf)
  >    * Text (.txt)
  >    * Word Documents (.docx, .doc)
  >    * PowerPoint Presentations (.pptx, .ppt)
  >* File size limit: The maximum file size supported for each individual file is 100 MB. Please ensure that your uploaded files do not exceed this limit to avoid request failures.
  
  - **Send a POST request** to `api/v1/parse` including the file you want to upload in the request body. Replace `api-key` with your personal API key. For the fastest processing, we recommend starting with the Lite mode.


   ``` shell
      curl https://api.easydoc.sh/api/v1/parse \
	-X POST \
	-H "api-key: your-api-key" \
	-F "file=@demo_document.pdf" \
	-F "mode=lite" \
   ```

   - **Response**: You will receive a `task_id` from the server response that you can use to track the status of the parsing task.

   For detailed API documentation and usage instructions, see [API Reference for POST /api/v1/parse](/docs/api-reference/parse.md).

   ---

   #### 2. **GET api/v1/parse/{task_id}/result**  
   This API allows you to retrieve the result of the parsing task you previously created.

 
   - **Send a GET request** to `api/v1/parse/{task_id}/result`, replacing  `{task_id}` with the task ID returned from the previous step.

   ``` bash
   curl "https://api.easydoc.sh/api/v1/parse/{task_id}/result"  \
    -X GET \
	-H "api-key: your-api-key"
   ```
   - **Response**: You will receive the parsing result once the task is complete.

   For more details on how to use this endpoint, see [API Reference for GET /api/v1/parse/{task_id}/result](/docs/api-reference/parse_result.md).

   --- 
