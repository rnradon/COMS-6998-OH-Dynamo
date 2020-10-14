import boto3
list_of_tas = [
    {
        'id': 1,
        'name': 'Rishabh',
        'day': 'Monday',
        'start_time': '9:00',
        'end_time': '11:00',
    },
    {
        'id': 2,
        'name': 'Reshma',
        'day': 'Tuesday',
        'start_time': '14:00',
        'end_time': '16:00'
    },
    {
        'id': 3,
        'name': 'Hyun',
        'day': 'Thursday',
        'start_time': '15:00',
        'end_time': '17:00'
    },
    {
        'id': 4,
        'name': 'Goutham',
        'day': 'Friday',
        'start_time': '16:00',
        'end_time': '18:00'
    }
]
def create_user(): 

    dynamodb = boto3.resource('dynamodb')
    
    table = dynamodb.Table('CourseAssistants')
    print("Table Status: ", table.table_status)
    
    for ta in list_of_tas:
        response = table.put_item(Item=ta)
        print(response)

create_user()