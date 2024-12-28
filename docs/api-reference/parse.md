## Overview

The `POST /api/v1/parse` endpoint lets you upload files to create parsing tasks. It uses the `AuthStrategyConstants.PARSE_API_AUTH` strategy for security, so you need to include a valid `api-key` in the request header.

---

## Request Parameters

### 1. `file` (MultipartFile)

- **What it does:** This is the file you want to parse.
- **Type:** `MultipartFile`
- **Required:** Yes
- **Validation Rules:**
  - The file must not be empty.
  - If the file is missing, the request will fail with an error.
- **Supported File Types:** [View supported file types](/docs/input.md).

### 3. `start_page` (Integer)

- **What it does:** Sets the page number where parsing starts (1-based index).
- **Type:** Integer
- **Required:** No
- **Validation Rules:**
  - Must be 1 or greater.
  - If both `start_page` and `end_page` are provided, `start_page` must be less than or equal to `end_page`.

### 4. `end_page` (Integer)

- **What it does:** Sets the page number where parsing ends.
- **Type:** Integer
- **Required:** No
- **Default Value:** `-1` (parses until the last page by default).
- **Validation Rules:**
  - Must be 1 or greater.
  - If `end_page` is greater than the actual number of pages in the document, the parsing will default to the last page of the document.

### 5. `mode` (String)

- **What it does:** Specifies the parsing method or mode.
- **Type:** String
- **Required:** Yes
- **Allowed Values:**
  - `lite`
  - `pro`
  - `premium`

---

## Request Headers

### 1. `api-key` (String)

- **What it does:** API key for authentication.
- **Required:** Yes

---

## Request Examples

### HTTP Request

```http
POST /api/v1/parse HTTP/1.1
Host: api.example.com
Content-Type: multipart/form-data
api-key: your-api-key

--boundary
Content-Disposition: form-data; name="file"; filename="document.pdf"
Content-Type: application/pdf

<file-content>
--boundary
Content-Disposition: form-data; name="start_page"

1
--boundary
Content-Disposition: form-data; name="end_page"

10
--boundary
Content-Disposition: form-data; name="mode"

pro
--boundary--
```

### cURL Example

```bash
curl -X POST \
  -H "api-key: your-api-key" \
  -F "file=@document.pdf" \
  -F "start_page=1" \
  -F "end_page=10" \
  -F "mode=pro" \
  https://api.easydoc.sh/api/v1/parse
```

---

## Response Format

### Successful Response

- **Status Code:** `200 OK`
- **Response Body:**

```json
{
    "success": true,
    "err_code": null,
    "err_message": null,
    "data": {
        "task_id": "*********************************"
    }
}
```

### Failed Response

- **Status Code:** `200 OK`
- **Response Body:**

```json
{
    "success": false,
    "err_code": "CONSOLE_UNAUTHORIZED",
    "err_message": "Unauthorized access to API service"
}
```

---

## Error Codes

| Error Code                | Error Message                      | Description                                                                      |
| ------------------------- | ---------------------------------- | -------------------------------------------------------------------------------- |
| `API_UNAUTHORIZED`        | Unauthorized access to API service | API key validation failed.                                                       |
| `INVALID_PARAMETER`       | Invalid parameter.                 | General parameter error, including missing or invalid values.                    |
| `INTERNAL_SERVER_ERROR`   | Internal server error.             | Triggered when the system encounters an unknown error.                           |
| `INSUFFICIENT_RESOURCES`  | Insufficient resources.            | Triggered when system resources (CPU, memory, or storage) are insufficient.      |
| `INVALID_DOCUMENT_FORMAT` | Invalid document format.           | Triggered when the uploaded file format is not supported or cannot be processed. |

---

## Notes

1. Ensure uploaded files meet security and size requirements.
2. The `mode` parameter determines the parsing method and affects both speed and accuracy.
3. Use the `start_page` and `end_page` parameters to parse specific sections of the document.

