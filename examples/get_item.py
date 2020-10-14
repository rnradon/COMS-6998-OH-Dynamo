import boto3

def get_item():
    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('CourseAssistants')      
    
    resp = table.get_item(
            Key={
                'id' : 1,
            }
        )
                
    if 'Item' in resp:
        print(resp['Item'])

get_item()