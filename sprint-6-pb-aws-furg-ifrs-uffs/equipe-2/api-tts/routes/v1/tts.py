import os, json
from utils import utils, s3, awsutils, polly

def v1_tts(event, context):
    try:
        data = json.loads(event['body'])
        ''' enable on local env:
        data = event
        '''

        if 'phrase' not in data or data['phrase'] == '': raise Exception('create item: \'phrase\' not specified')
        
        # aws clients 
        pollyc     = awsutils.client_init('polly')
        s3c        = awsutils.client_init('s3')

        # phrase format: without extra spaces and all lowercase
        fmt_phrase = utils.fmt_message(data['phrase'])
        # filename: hash based on formated phrase
        filename   = utils.get_hash(fmt_phrase)

        # get and persis synthesize message into audio file
        polly_audio = polly.synth_speech(pollyc, fmt_phrase)
        audio_url   = s3.upload(s3c, polly_audio, 'v1/', filename, 'mp3')
        
        # here we can approximate the timestamp from the one on s3 
        timestamp = utils.get_timestamp()

        res_body = {
            "received_phrase":  data['phrase'], 
            "url_to_audio":     audio_url,
            "created_audio":    timestamp
        }
        return {"statusCode": 200, "body": json.dumps(res_body)}
    except Exception as error:
        return {"statusCode": 500, "body": f"Couldn't {error}: an error ocurred."}