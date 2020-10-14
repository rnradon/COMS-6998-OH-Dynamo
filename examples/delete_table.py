import boto3

def delete_table():
    dynamodb = boto3.client('dynamodb')
    
    table = 'CourseAssistants'     
    
    response = dynamodb.delete_table(
        TableName=table
    )

delete_table()