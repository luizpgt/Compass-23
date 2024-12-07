import os, json
from utils import utils, awsutils, s3, polly, dynamodb

def v2_tts(event, context):
    try:
        data = json.loads(event['body'])
        ''' enable on local env:
        data = event
        '''

        if 'phrase' not in data or data['phrase'] == '': raise Exception('create item: \'phrase\' not specified')
        
        # aws clients 
        pollyc      = awsutils.client_init('polly')
        s3c         = awsutils.client_init('s3')
        dynamodbc   = awsutils.client_init('dynamodb')

        # phrase format: without extra spaces and all lowercase
        fmt_phrase = utils.fmt_message(data['phrase'])
        # fhash        : hash based on formated phrase
        fhash      = utils.get_hash(fmt_phrase)

        # get and persis synthesize message into audio file
        polly_audio = polly.synth_speech(pollyc, fmt_phrase)
        audio_url   = s3.upload(s3c, polly_audio, 'v2/', fhash, 'mp3')
        
        # here we can approximate the timestamp on s3 (bucket) 
        timestamp  = utils.get_timestamp()

        # persists reference audio data at dynamodb
        try: 
            # if cannot persist, returns an error to remove unreferenced item from s3
            dyndb_info = dynamodb.put_item(dynamodbc, fhash, timestamp, audio_url, data['phrase'])
        except Exception as error:
            try:
                t = s3.delete(s3c, 'v2/', fhash, 'mp3')
            except Exception as error2:
                raise Exception(f'{error}, neither {error2}')
            raise Exception(f'{error} all previous steps undone')

        res_body = {
            "received_phrase":  data['phrase'], 
            "url_to_audio":     audio_url,
            "created_audio":    timestamp,
            "unique_id":        fhash
        }
        return {"statusCode": 200, "body": json.dumps(res_body)}
    except Exception as error:
        return {"statusCode": 500, "body": f"Couldn't {error}: an error ocurred."}