import paramiko 
import sys
from exceptions import SSHConnectionError, FileUploadError,ParameterValidationError

def validate_params(hostname: str, username: str, password: str, remote_file_path: str, file_path: str):
    if not hostname or not username or not password or not remote_file_path or not file_path:
        raise ParameterValidationError("Please provide all required parameters: hostname, username, password, remote_file_path, file_path")
    
       
def create_ssh_client(hostname:str, username:str, password:str):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh_client.connect(hostname=hostname, username=username, password=password)
    except paramiko.SSHException as e:
        raise SSHConnectionError(f"Failed to establish SSH connection: {e}")
    return ssh_client


def upload_file(ssh_client, local_file_path,remote_path):
    try:
        ftp_client = ssh_client.open_sftp()
        ftp_client.put(local_file_path, remote_path)
        ftp_client.close()
    except Exception as e:
        raise FileUploadError(f"Failed to upload file: {e}")
    finally:
        ssh_client.close()
        
        
def send_file(hostname:str,username:str,password:str,remote_file_path:str,file_path:str):
    validate_params(hostname, username, password, remote_file_path, file_path)
    ssh_client = create_ssh_client(hostname, username, password)
    upload_file(ssh_client, file_path,remote_file_path)
    return True
    







