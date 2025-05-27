import boto3
import time # Required for confirmation of subscription

# This script creates an EC2 instance in the 'ap-south-1' region using Boto3.
ec2 = boto3.client('ec2', region_name='ap-south-1')
instance = ec2.run_instances(
    ImageId='ami-0e35ddab05955cf57',
    InstanceType='t2.micro',
    KeyName='general-key-pair',
    MinCount=1,
    MaxCount=1,
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [{'Key': 'Name', 'Value': 'project-ec2-s3'}]
        }
    ]
)
print(f"Instance created with ID: {instance['Instances'][0]['InstanceId']}\n")

# Create S3 bucket
s3 = boto3.client('s3')
bucket_name = 'ec2-bucket-project-dakshsawhneyy'
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)
print(f"Bucket created with name: {bucket_name}")

# Upload a file to the S3 bucket
s3.upload_file('./files/index.html', bucket_name, 'index3.html')
print("File uploaded successfully to S3 bucket.\n")

# Download the file from the S3 bucket
s3.download_file(bucket_name, 'index3.html', './files/downloaded_file3.txt')
print("File downloaded successfully from S3 bucket.\n")

# List Objects in S3
response = s3.list_objects_v2( Bucket=bucket_name )
if 'Contents' in response:
    for obj in response['Contents']:
        print(f"Name of Objects is: {obj["Key"]}\n")
        
# Delete All files from S3 Bucket
responsee = s3.list_objects_v2(Bucket=bucket_name)
if 'Contents' in responsee:
    for obj in responsee['Contents']:
        print("Deleting all files from bucket.....\n")
        s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
        print("Files Deleted Successfully\n")

# Delete S3 Bucket
print(f"Deleting Bucket.... {bucket_name}\n"),
s3.delete_bucket(Bucket=bucket_name,)
print(f"{bucket_name} deleted successfully.... \n")

# Terminate Instance
instance_id = instance['Instances'][0]['InstanceId']
responce = ec2.terminate_instances(
    InstanceIds = [instance_id]
)
# print(responce)
print(f"Terminating instance: {instance_id} \n\n")

# SNS Service
client = boto3.client('sns', region_name='ap-south-1')

# Create Topic
response = client.create_topic(Name = 'python-topic-creation')
topic_arn = response['TopicArn']
print(f"Topic created with ARN: {topic_arn}\n")

# Subscribe to topic
responce = client.subscribe(
    TopicArn=topic_arn,
    Protocol='email',
    Endpoint='dakshsawhneyy@gmail.com'   
)
print(f"Subscribed to {topic_arn} sent to your email for confirmation.\n")

# Wait for confirmation
while True:
    subs = client.list_subscriptions_by_topic(TopicArn=topic_arn)
    subs_arn = subs['Subscriptions'][0]['SubscriptionArn']
    if subs_arn != 'PendingConfirmation':
        print("Subscription confirmed.")
        break
    else:
        print("Waiting for subscription confirmation...")
        time.sleep(5)   # sleep for 5 seconds
        
# Publish A Message
message = client.publish(
    TopicArn = topic_arn,
    Subject = "Finally created An SNS Notification",
    Message = "I am building myself so strong that none can beat me"
)
print("Message Sent Successfully\n")
