from fastapi import FastAPI, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pandas as pd
import os
import time
from io import StringIO

# Pydantic models for request and response
class Data(BaseModel):
    id: int
    name: str
    email: str

class GenericResponse(BaseModel):
    message: str

# FastAPI app instance
app = FastAPI()

# Root endpoint
@app.get("/", response_class=HTMLResponse)
async def root() -> str:
    return "<h1>Hello, <br> This is the New Server!!</h1>"

# Upload CSV endpoint
@app.post("/upload-csv", status_code=201)
async def upload_csv(file: UploadFile = File(...)):
    try:
        # Process the uploaded CSV file
        content = await file.read()
        df = pd.read_csv(StringIO(content.decode('utf-8')))

        # Create 'files' directory if it doesn't exist
        os.makedirs('files', exist_ok=True)

        # Save the DataFrame to a CSV file with the current timestamp
        timestamp_str = time.strftime("%Y-%m-%d_%H-%M-%S")  
        file_path = f"files/{timestamp_str}.csv"
        df.to_csv(file_path, index=False)

        # Return a response using the GenericResponse model
        return GenericResponse(message=f"CSV file saved to {file_path}")
    except pd.errors.EmptyDataError:
        # Handle the case where the uploaded CSV file is empty
        raise HTTPException(status_code=422, detail="The uploaded CSV file is empty")
    except Exception as e:
        # If there's any other exception, raise an HTTPException with a 500 status code and the error message
        raise HTTPException(status_code=500, detail=str(e))

# Run the application with host '0.0.0.0' and a specific port, e.g., 8000
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2121)
