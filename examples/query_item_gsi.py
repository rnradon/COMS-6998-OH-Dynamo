import boto3
from boto3.dynamodb.conditions import Key

def query_data_with_gsi():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('CourseAssistants')
    
    response = table.query(
        IndexName='name',
        KeyConditionExpression=Key('name').eq('Rishabh')
    )
    
    print(response['Items'][0])

query_data_with_gsi()