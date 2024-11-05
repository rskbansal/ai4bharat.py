from constants import *
from errors import *
from utils import *
import requests
import base64

def tts(text, source_lang, out_file = None, voice = 'male', sampling_rate = 16000):
    source_lang = source_lang.strip().lower()
    voice = voice.strip().lower()
    sampling_rate = int(sampling_rate)

    if sampling_rate < 8000:
        raise AudioError(sampling_rate)

    if LANGUAGES.get(source_lang) == None or LANGUAGES[source_lang]['tts_service'] == None:
        raise LanguageError('source', source_lang)
    if voice != 'male' and voice != 'female':
        raise VoiceError(voice)
    
    payload = {
        'sourceLanguage': LANGUAGES[source_lang]['code'],
        'input': text,
        'task': 'tts',
        'serviceId': LANGUAGES[source_lang]['tts_service'],
        'samplingRate': sampling_rate,
        'gender': voice,
        'track': False
    }

    resp = requests.post(TTS_ENDPOINT, json = payload)
    status_code = resp.status_code

    if status_code != 200:
        raise APIError(status_code)
    
    resp = resp.json()
    audio_data = resp['audio'][0]['audioContent']

    if out_file == None:
        out_file = gen_tts_filename(source_lang)

    with open(out_file, 'wb') as f:
        f.write(base64.b64decode(audio_data))

    return None
