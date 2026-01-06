import json
import os

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from the AWS Cloud (via Terraform)!')
    }
