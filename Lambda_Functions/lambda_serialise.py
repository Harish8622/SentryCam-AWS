import json
import base64
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the S3 key and bucket from the event input
    key = event["s3_key"]
    bucket = event["s3_bucket"]
    
    # Download the image to /tmp, lambda has temporary directory
    download_path = "/tmp/image.png"
    s3.download_file(bucket, key, download_path)
    
    # Read the image and encode it to base64
    with open(download_path, "rb") as f:
        image_data = base64.b64encode(f.read()).decode("utf-8")

    event["image_data"] = image_data
    event["s3_bucket"] = bucket
    event["s3_key"] = key
    event["inferences"] = []
    # Return the event with the image_data added
    return event
