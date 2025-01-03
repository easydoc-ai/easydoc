# EasyDoc API Examples

This module provides example scripts for interacting with the EasyDoc API. It demonstrates how to:
1. Upload files for parsing.
2. Retrieve parsing results.

## Prerequisites

1. **API Key**: Obtain your API key from the [EasyDoc API Key Management Page](https://platform.easydoc.sh/api-keys).
2. **Python**: Install Python 3.7+ on your machine.
3. **Dependencies**: Install required libraries with `pip install requests`.

## Setup

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-repo-name.git
   cd your-repo-name/examples
   ```

2. Replace the placeholder `your-api-key` in `upload_and_parse.py` with your actual API key.

3. Ensure the file you want to parse is accessible on your local machine.

## Usage

### Upload and Parse a File

Run the script with the following command:
```bash
python upload_and_parse.py
```

This script will:
1. Upload a file to create a parsing task.
2. Poll the API to check the parsing task status.
3. Print the parsing result once the task is complete.

### Example Output

```bash
Uploading path/to/your/document.pdf...
File uploaded successfully. Task ID: abc123xyz
Fetching result for Task ID: abc123xyz...
Task status: PENDING. Retrying in 5 seconds...
Task status: PROGRESSING. Retrying in 5 seconds...
Parsing completed successfully.
Parsing Result:
{
    "content": "Extracted text from your document..."
}
```

## Notes

- Use the `mode` parameter (`lite`, `pro`, `premium`) to control parsing speed and accuracy.
- Adjust `start_page` and `end_page` to parse specific sections of the document.

## Reference Documentation

- [POST /api/v1/parse](docs/api-reference/parse.md)
- [GET /api/v1/parse/{task_id}/result](docs/api-reference/parse_result.md)

