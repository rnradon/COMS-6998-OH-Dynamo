import boto3

def delete_user():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('CourseAssistants')
    
    response = table.delete_item(
        Key={
            'id': 1,
        },
    )
    print(response)

delete_user()
