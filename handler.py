import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Demo pipeline is successfully deployed test2",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
