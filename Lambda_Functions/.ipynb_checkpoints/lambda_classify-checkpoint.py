import json
import boto3
import base64

# update endpoint here when deployed
ENDPOINT = "vehicle-detector-endpoint-09-04-25"

def lambda_handler(event, context):
    # Decode base64 image
    body = json.loads(event['body']
    image = base64.b64decode(body["image_data"])

    # Use boto3 SageMaker runtime client
    client = boto3.client("sagemaker-runtime")

    response = client.invoke_endpoint(
        EndpointName=ENDPOINT,
        ContentType="image/png",
        Body=image
    )

    # Parse response
    inferences = json.loads(response["Body"].read().decode())

    # Add inferences to event
    event["inferences"] = inferences

    return {
        "statusCode": 200,
        "body": json.dumps(event)
    }