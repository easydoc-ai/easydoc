### Input

#### Supported Input Formats

The EasyDoc API supports the following input file formats:

- **PDF** (.pdf)
- **Text** (.txt)
- **Word Documents** (.docx, .doc)
- **PowerPoint Presentations** (.pptx, .ppt)

---

#### File Size Limit

The maximum file size supported for each individual file is **100 MB**. Please ensure that your uploaded files do not exceed this limit to avoid request failures.

---

#### Input Parameter Explanation
  
- **Required Parameters**:
  - **api-key**: The API key for authenticating your request. Include it in the request header.
  - **File**: The document to upload for parsing. Include it in the request body when sending a POST request to `api/v1/parse`.
- **Optional Parameters**:
  See [API Reference for Input Parameters](/docs/api-reference/parse.md).

---

