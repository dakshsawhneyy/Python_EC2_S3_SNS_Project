# AWS Automation Project with Boto3

This project automates the lifecycle of AWS services using Python and Boto3. It includes EC2 instance creation, S3 bucket management, SNS notifications, and complete resource cleanup.

## Features

🟣 Launch EC2 instance  
🟣 Create and delete S3 bucket  
🟣 Upload and download files to/from S3  
🟣 Create and confirm SNS topic subscription via email  
🟣 Send notification after confirmation  
🟣 Terminate EC2 instance  
🟣 Clean and readable Python code  

## Requirements

- Python 3.x  
- Boto3  
- AWS credentials configured via AWS CLI or environment variables  
- Internet connection  
- Valid AWS account with permissions for EC2, S3, SNS

## Setup

1. Install Boto3 if not already:
    ```bash
    pip install boto3
    ```

2. Configure your AWS credentials (only once):
    ```bash
    aws configure
    ```

3. Place an HTML file inside a folder named `files/` named `index.html`

4. Run the Python script.

## Folder Structure

```
project-folder/
│
├── files/
│   ├── index.html         # File to upload to S3
│
├── main.py                # Python script to automate the AWS workflow
├── README.md              # You're here!
```

## What it Does

- Creates an EC2 instance with specified tags and key pair.
- Creates an S3 bucket and uploads a test HTML file.
- Downloads the uploaded file to verify it works.
- Creates an SNS topic and subscribes an email endpoint.
- Waits until email is confirmed (polling every 5 seconds).
- Sends a notification once confirmed.
- Deletes all uploaded files and the S3 bucket.
- Terminates the EC2 instance.

## Notes

- SNS subscription requires you to confirm the email via inbox.
- Use IAM roles if you want to avoid using access/secret keys.
- Be cautious about creating duplicate resources (e.g., bucket names must be globally unique).

## Author

Daksh Sawhney — Built with 💪 and Python 
