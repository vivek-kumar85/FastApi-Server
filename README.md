# FastAPI CSV File Upload

This project demonstrates a FastAPI application that allows users to upload a CSV file. The uploaded file is processed, and its content is saved with a timestamp in the "files" directory.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the FastAPI Server](#running-the-fastapi-server)
  - [Uploading a CSV File](#uploading-a-csv-file)
- [License](#license)

## Introduction

This FastAPI application provides a simple endpoint for uploading CSV files. It includes error handling for cases where the uploaded file is empty or encounters other exceptions.

## Features

- File upload with timestamped storage
- Handling of empty CSV files
- Error handling with appropriate HTTP status codes

## Getting Started

Follow these instructions to set up and run the FastAPI application locally.

### Prerequisites

- Python 3.9.12
- FastAPI
- Uvicorn
- Pandas

### Installation

1. Clone the repository:

   ```bash
   https://github.com/vivek-kumar85/FastApi-Server.git

   ```
  
2. Navigate to the project directory:
```
  cd FastApi-server

  ```

3. Install dependencies:
```
   pip install -r requirements.txt 
   ```


   ### Usage
#### Running the FastAPI Server
Run the FastAPI server with the following command:
```
 uvicorn main:app --host 0.0.0.0 --port 2121 --reload

```

## Uploading a CSV File
Example Python script to upload a CSV file:

### Uploading a CSV File

To upload a CSV file to the FastAPI endpoint, you can use the following Python script:

```Python
import requests

# URL of the FastAPI endpoint
url = "http://103.97.164.81:2121/upload-csv"

# Path to the CSV file you want to send
csv_file_path = "path/to/your/csv/file.csv"

# Open the CSV file and read its content
with open(csv_file_path, "rb") as file:
    # Create a dictionary with the file data
    files = {"file": (csv_file_path, file)}

    # Send the POST request with the CSV file
    response = requests.post(url, files=files)

# Print the response status code and content
print("Status Code:", response.status_code)
print("Response Content:", response.text)

```

### License

[MIT](https://choosealicense.com/licenses/mit/)




