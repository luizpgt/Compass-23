import os

def get_item(client, item_uid):
    try:
        response = client.get_item(
            Key={
                'unique_id': {
                    'S': item_uid,
                },
            },
            ConsistentRead=True,
            TableName=os.environ.get("DYNAMODB_TABLE"),
        )    
        return response
    except:
        raise Exception('get item reference from dynamo db table')


def put_item(client, item_uid, item_timst, item_audio_url, item_phrase):
    try:
        response = client.put_item(
            Item={
                'unique_id': {
                    'S': item_uid,
                },
                'created_audio': {
                    'S': item_timst,
                },
                'received_phrase': {
                    'S': item_phrase,
                },
                'url_to_audio': {
                    'S': item_audio_url,
                },
            },
            ReturnConsumedCapacity='TOTAL',
            TableName=os.environ.get("DYNAMODB_TABLE"),
        )
        return response
    except:
        raise Exception('upload item reference into dynamo db table')
