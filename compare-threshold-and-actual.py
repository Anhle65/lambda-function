import json
import boto3
from datetime import datetime, date
import random


client = boto3.client('dynamodb')

def lambda_handler(event, context):
  
  isDateNull = event.get('date', '')
  if isDateNull == '':
    event['date'] = str(date.today())
    print("Date is null so getting date.today ", isDateNull)
  

  timestamp = str(datetime.now())
  isThresholdNull = event.get('threshold', '')
  if isThresholdNull == '':
    event['threshold'] = 14200
  else:
    store_new_request(event)
  threshold = event['threshold']
  if float(event['price']) <= float(threshold):
    event['condition'] = "true"
  else:
    event['condition'] = "false"
  return event
def store_new_request(event):
    character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    id = ''.join([random.choice(character) for i in range(20)])
    # time = datetime.now().strftime("%H:%M:%S")
    dates = str(date.today())
    timestamp = str(datetime.now())
    data = client.put_item(
    TableName='history_request',
    Item={
        'Id': {
          'S': id
        },
        'date':{
          'S': dates
        },
        'threshold': {
          'N': event['threshold']
        },
        'datestamp':{
          'S': timestamp
          }
    }
    )
    print ("finish update")