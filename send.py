

import requests

# URL of the FastAPI endpoint
url = "http://103.97.164.81:2121/upload-csv"  # Replace with your actual URL

# Path to the CSV file you want to send
csv_file_path = "F:/Vivek_drive_F/Wilo_project/fft-stuff/data/FFT2.csv"  # Replace with the actual path

# Open the CSV file and read its content
with open(csv_file_path, "rb") as file:
    # Create a dictionary with the file data
    files = {"file": (csv_file_path, file)}

    # Send the POST request with the CSV file
    response = requests.post(url, files=files)

# Print the response status code and content
print("Status Code:", response.status_code)
print("Response Content:", response.text)
