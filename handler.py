import json


def hello(event, context):
    body = {
        "message": "Go Serverless v3.0! Demo pipeline is successfully deployed first",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
