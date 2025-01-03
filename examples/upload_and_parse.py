import requests
import time

# API Base URL
BASE_URL = "https://api.easydoc.sh/api/v1"

# Your API Key (replace with your own key)
API_KEY = "your-api-key"

# Upload a file and create a parsing task
def upload_file(file_path, mode="lite", start_page=None, end_page=None):
    url = f"{BASE_URL}/parse"
    headers = {"api-key": API_KEY}
    files = {"file": open(file_path, "rb")}
    data = {"mode": mode}
    
    if start_page:
        data["start_page"] = start_page
    if end_page:
        data["end_page"] = end_page

    print(f"Uploading {file_path}...")
    response = requests.post(url, headers=headers, files=files, data=data)
    if response.status_code == 200 and response.json().get("success"):
        task_id = response.json()["data"]["task_id"]
        print(f"File uploaded successfully. Task ID: {task_id}")
        return task_id
    else:
        print(f"Error uploading file: {response.json()}")
        return None

# Get the parsing result
def get_parse_result(task_id):
    url = f"{BASE_URL}/parse/{task_id}/result"
    headers = {"api-key": API_KEY}

    print(f"Fetching result for Task ID: {task_id}...")
    while True:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            if data["success"]:
                status = data["data"]["task_status"]
                if status == "SUCCESS":
                    print("Parsing completed successfully.")
                    return data["data"]["task_result"]
                elif status in ["PENDING", "PROGRESSING"]:
                    print(f"Task status: {status}. Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    print(f"Task failed with status: {status}.")
                    return None
            else:
                print(f"Error: {data['errMessage']}")
                return None
        else:
            print(f"Error fetching result: {response.status_code}")
            return None

if __name__ == "__main__":
    # Replace with the path to your file
    file_path = "path/to/your/document.pdf"
    
    # Step 1: Upload the file
    task_id = upload_file(file_path, mode="lite", start_page=1, end_page=None)
    
    # Step 2: Retrieve the parsing result
    if task_id:
        result = get_parse_result(task_id)
        if result:
            print("Parsing Result:")
            print(result)
