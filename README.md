# MerlinTransfer

<img src="https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/f1c0947c-73d5-409d-ae9d-f9c9c07abae8/d8wk9fg-736edf92-c4f3-4c4b-91ba-2bab75d3396b.png/v1/fill/w_1024,h_1243/merlin_clipart_by_disneyfreak19_d8wk9fg-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTI0MyIsInBhdGgiOiJcL2ZcL2YxYzA5NDdjLTczZDUtNDA5ZC1hZTlkLWY5YzljMDdhYmFlOFwvZDh3azlmZy03MzZlZGY5Mi1jNGYzLTRjNGItOTFiYS0yYmFiNzVkMzM5NmIucG5nIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.QqpyYBgsh2ZShDD4gl5nysxZZskUDN2-oRiTqV3_txw" alt="merlin_img" width="300" height="300">



MerlinTransfer is a Python package designed for securely uploading files to a remote server using SSH. It leverages `paramiko` for SSH connection management and allows easy customization through Python function calls.

## Features

- **SSH File Upload**: Securely upload files to a specified remote server.
- **Customizable SSH Connection**: Configure hostname, username, and password for SSH connections.
- **Error Handling**: Provides basic error handling for connection and file transfer operations.

## Requirements

- Python 3.6 and above

## Installation

Install MerlinTransfer using pip:

```sh
pip install git+<link_to_this_repo>@main
```

## Usage
Import MerlinTransfer into your Python script:

```python
from merlintransfer import send_file
```

# Example usage
```python

hostname = "your_ssh_hostname_or_ip"
username = "your_ssh_username"
password = "your_ssh_password"
remote_file_path = "/path/on/remote/server/file.txt"
local_file_path = "path/to/local/file.txt"

try:
    send_file(hostname, username, password, remote_file_path, local_file_path)
except SSHConnectionError as e:
    print(f"SSH Connection Error: {e}")
except FileUploadError as e:
    print(f"File Upload Error: {e}")
except ParameterValidationError as e:
    print(f"Parameter Validation Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

```

Function send_file Parameters:

* hostname: The hostname or IP address of the remote SSH server.
* username: The username used for SSH authentication.
* password: The password used for SSH authentication.
* remote_file_path: The path where the file will be uploaded on the remote server.
* file_path: The local path of the file to upload.

# Exceptions

`SSHConnectionError`

Raised when there is an issue with the SSH connection.

`FileUploadError`

Raised when there is an error during the file upload process.

`ParameterValidationError`

Raised when there are invalid parameters provided to the send_file function.

