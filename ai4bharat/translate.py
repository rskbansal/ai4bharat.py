from .constants import *
from .errors import *
from .utils import *
import requests

def translate(text, source_lang, target_lang):
    """Translates text from one language to another.

    Arguments:
        text (str): Text to be translated.
        source_lang (str): Language of the provided text.
        target_lang (str): Language to which the input text is to be translated.

    Returns:
        str: The translated text.
    """
    source_lang = source_lang.strip().lower()
    target_lang = target_lang.strip().lower()

    if LANGUAGES.get(source_lang) == None or source_lang == 'rajasthani':
        raise LanguageError('source', source_lang)
    if LANGUAGES.get(target_lang) == None or target_lang == 'rajasthani':
        raise LanguageError('target', source_lang)

    payload = {
        'sourceLanguage': LANGUAGES[source_lang]['code'],
        'targetLanguage': LANGUAGES[target_lang]['code'],
        'input': text,
        'task': 'translation',
        'serviceId': 'ai4bharat/indictrans--gpu-t4',
        'track': False
    }

    resp = requests.post(TRANSLATE_ENDPOINT, json=payload)
    status_code = resp.status_code

    if status_code != 200:
        raise APIError(status_code)
    
    resp = resp.json()
    translated_text = resp['output'][0]['target']

    return translated_text