import boto3
import json

sns_topic_arn = 'my_arn'

def lambda_handler(event, context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']

        print(f"New object added to S3: {bucket}/{key}")

        sns_client = boto3.client('sns')
        message = f"New object added to S3: {bucket}/{key}"
        sns_client.publish(TopicArn=sns_topic_arn, Message=message, Subject="S3 Notification")

    return {
        'statusCode': 200,
        'body': json.dumps('S3 event processing complete.')
    }
