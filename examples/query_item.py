import boto3
from boto3.dynamodb.conditions import Key

def query():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('CourseAssistants')      
    
    resp = table.query(
        KeyConditionExpression=Key('id').eq(1)
    )
                
    if 'Items' in resp:
        print(resp['Items'][0])

query()