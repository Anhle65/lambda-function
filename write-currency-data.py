import boto3
from datetime import datetime, date
import random
client = boto3.client('dynamodb')

def lambda_handler(event, context):
    character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    id = ''.join([random.choice(character) for i in range(20)])
    dates = str(date.today())
    timestamp = str(datetime.now())
    data = client.put_item(
    TableName='data_exchange_rate',
    Item={
        'Id': {
          'S': id
        },
        'date':{
          'S': dates
        },
        'price': {
          'N': event['price']
        },
        'datestamp':{
          'S': timestamp
          }
    }
    )
    return event