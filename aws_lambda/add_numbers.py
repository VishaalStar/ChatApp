import json

def lambda_handler(event, context):
    try:
        num1 = float(event['num1'])
        num2 = float(event['num2'])
        result = num1 + num2
        return {
            'statusCode': 200,
            'body': json.dumps(f'The sum of {num1} and {num2} is {result}')
        }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Please provide two numbers (num1 and num2) in the event')
        }
    except ValueError:
        return {
            'statusCode': 400,
            'body': json.dumps('Please ensure both inputs are valid numbers')
        }