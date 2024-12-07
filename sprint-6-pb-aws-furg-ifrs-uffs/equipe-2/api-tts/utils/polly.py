def synth_speech(client, message):
    try:
        res = client.synthesize_speech(Text=message,
                                    OutputFormat="mp3",
                                    LanguageCode="pt-BR",
                                    VoiceId="Camila",
                                    Engine="neural")
        res = res['AudioStream'].read()
        return res
    except: 
        raise Exception('synthesize message into audio file')