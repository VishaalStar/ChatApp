import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        file_content = base64.b64decode(event['file_content'])
        file_name = event['file_name']
        bucket_name = event['bucket_name']
        
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} successfully uploaded to {bucket_name}')
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Please provide file_content, file_name, and bucket_name in the event')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }