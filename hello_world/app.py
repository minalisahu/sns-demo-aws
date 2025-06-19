import json
import boto3
import os

sns = boto3.client('sns')

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        message = body.get('message', 'Hello from Lambda!')
        topic_arn = os.environ.get('SNS_TOPIC_ARN')

        response = sns.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject="Demo Notification"
        )

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Message published successfully!",
                "response": response
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
