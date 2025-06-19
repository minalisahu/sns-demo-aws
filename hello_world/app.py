# Import required modules
import json               # For parsing and constructing JSON data
import boto3              # AWS SDK for Python to interact with AWS services
import os                 # For accessing environment variables

# Create an SNS client using boto3
sns = boto3.client('sns')

# Main Lambda handler function
def lambda_handler(event, context):
    try:
        # Parse the incoming JSON body from the API Gateway request
        body = json.loads(event['body'])

        # Get the 'message' key from the request body, with a default fallback message
        message = body.get('message', 'Hello from Lambda!')

        # Get the SNS topic ARN from environment variables (set in template.yaml)
        topic_arn = os.environ.get('SNS_TOPIC_ARN')

        # Publish the message to the specified SNS topic
        response = sns.publish(
            TopicArn=topic_arn,            # ARN of the SNS topic
            Message=message,               # Actual message content
            Subject="Demo Notification"    # Optional subject (used in email, etc.)
        )

        # Return a success response back to API Gateway
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Message published successfully!",
                "response": response       # Includes MessageId and metadata
            })
        }

    # Handle any errors and return a 500 response with the error message
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)            # Convert exception to a string
            })
        }
