# MerlinTransfer

MerlinTransfer is a Python package designed for securely uploading files to a remote server using SSH. It leverages `paramiko` for SSH connection management and allows easy customization through Python function calls.

## Features

- **SSH File Upload**: Securely upload files to a specified remote server.
- **Customizable SSH Connection**: Configure hostname, username, and password for SSH connections.
- **Error Handling**: Provides basic error handling for connection and file transfer operations.

## Requirements

- Python 3.6 and above
- `paramiko` library

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

send_file(hostname, username, password, remote_file_path, local_file_path)

```

Function send_file Parameters:

* hostname: The hostname or IP address of the remote SSH server.
* username: The username used for SSH authentication.
* password: The password used for SSH authentication.
* remote_file_path: The path where the file will be uploaded on the remote server.
* file_path: The local path of the file to upload.

