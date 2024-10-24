from constants import *
from errors import *
from utils import *
import requests

def translate(text, source_lang, target_lang):
    if LANGUAGES.get(source_lang) == None:
        raise LanguageError(f'Invalid source language - "{source_lang}"')
    if LANGUAGES.get(target_lang) == None:
        raise LanguageError(f'Invalid target language - "{target_lang}"')
    
    payload = {
        'sourceLanguage': LANGUAGES[source_lang]['code'],
        'targetLanguage': LANGUAGES[target_lang]['code'],
        'input': text,
        'task': 'translation',
        'serviceId': 'ai4bharat/indictrans--gpu-t4',
        'track': False
    }

    resp = requests.post(TRANSLATE_ENDPOINT, json=payload)
    resp = resp.json()
    translated_text = resp['output'][0]['target']

    return translated_text