import json

def lambda_handler(event, context):
    response = {
        "message": "Application deployed successfully",
        "status": "healthy"
    }

    return {
        "statusCode": 200,
        "body": json.dumps(response)
    }

