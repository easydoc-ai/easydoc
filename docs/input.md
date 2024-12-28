### Input

#### Supported Input Formats

The Easydoc API supports the following input file formats:

- **PDF** (.pdf)
- **Text** (.txt)
- **Word Documents** (.docx, .doc)
- **Excel Spreadsheets** (.xlsx, .xls)
- **PowerPoint Presentations** (.pptx, .ppt)

These formats are commonly used for document parsing tasks, allowing you to upload and process a wide range of file types.

---

#### File Size Limit

The maximum file size supported for each individual file is **100 MB**. Please ensure that your uploaded files do not exceed this limit to avoid request failures.

---

#### Input Parameter Explanation
  
- **Required Parameters**:
  - **api-key**: The API key for authenticating your request. Include this in the request header.
  - **File**: The file you wish to upload for parsing. It should be included in the request body when sending a POST request to `api/v1/parse`.
- **Optional Parameters**:
  refer to the [API Reference for Input Parameters](/docs/api-reference/parse.md).

---

