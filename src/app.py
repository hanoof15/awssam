import json

def lambda_handler(event, context):

    if event.get("queryStringParameters") ]:
        a= event["queryStringParameters"]["a"]
        b= event["queryStringParameters"]["b"]
    

    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({"message": int(a)+int(b)})
    }
