import os
import json
import boto3

def lambda_handler(event, context):
    
    s3_bucket = event['Records'][0]['s3']['bucket']['name']
    s3_object_key = event['Records'][0]['s3']['object']['key']
    s3_upload_time = event['Records'][0]['eventTime']
    uploader = event['Records'][0]['userIdentity']['principalId']
    
    print(event)
    
    subject = "New object uploaded to S3"
    body = f"HObject uploaded to S3 bucket '{s3_bucket}' with key '{s3_object_key}' at '{s3_upload_time} by '{uploader}'."
    sns_arn = os.environ['SNS_TOPIC_ARN']
    
    sns_client = boto3.client('sns')
    
    sns_client.publish(
        TopicArn=sns_arn,
        Subject=subject,
        Message=body
    )