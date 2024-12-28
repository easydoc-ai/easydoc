## Overview

The `GET /api/v1/parse/{task_id}/result` endpoint allows you to retrieve the result of a parsing task. This endpoint is protected by the `AuthStrategyConstants.PARSE_API_AUTH` strategy, so you must include a valid `api-key` in the request header for authentication.

---

## Request Parameters

### 1. `task_id` (PathVariable)

- **What it does:** The unique identifier of the parsing task.
- **Type:** String
- **Required:** Yes

---

## Request Headers

### 1. `api-key` (String)

- **What it does:** API key for authentication.
- **Required:** Yes

---

## Request Examples

### HTTP Request

```http
GET /api/v1/parse/{task_id}/result HTTP/1.1
Host: api.example.com
api-key: your-api-key
Content-Type: application/json
```

### cURL Example

```bash
curl -X GET "https://api.easydoc.sh/api/v1/parse/{task_id}/result" \
  -H "api-key: your-api-key"
```

---

## Response Format

### Successful Response

- **Status Code:** `200 OK`
- **Response Body:**

```json
{
    "success": true,
    "errCode": null,
    "errMessage": null,
    "data": {
        "taskId": "*********************************", // Unique task ID
        "status": "PENDING", // PENDING, SUCCESS, ERROR, PROGRESSING
        "taskResult": {
            // Parsed data, this field has a value when data.status == SUCCESS
        }
    }
}
```

### Failed Response

- **Status Code:** `200 OK`
- **Response Body:**

```json
{
    "success": false,
    "errCode": "CONSOLE_UNAUTHORIZED",
    "errMessage": "Unauthorized access to API service"
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

