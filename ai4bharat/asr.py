from .constants import *
from .errors import *
from .utils import *
import requests
import base64

def asr(audio_file, source_lang, domain = 'general'):
    """Automatic Speech Recognition processes the audio file and returns the recognized text.

    Arguments:
        audio_file (str): Path to the audio file.
        source_lang (str): Language of the audio file.
        domain (str, optional): Specific area of speech for specialized vocabulary & patterns. Defaults to 'general'.

    Returns:
        str: The recognized text.
    """
    source_lang = source_lang.strip().lower()
    domain = domain.strip().lower()

    with open(audio_file, 'rb') as f:
        data = f.read()

    if LANGUAGES.get(source_lang) == None or source_lang == 'rajasthani':
        raise LanguageError('source', source_lang)
    if domain not in ASR_DOMAINS:
        raise DomainError(domain)
    
    sampling_rate = get_sampling_rate(audio_file)
    
    payload = {
        'sourceLanguage': LANGUAGES[source_lang]['code'],
        'audioContent': base64.b64encode(data).decode(),
        'task': 'asr',
        'domain': domain,
        'serviceId': 'ai4bharat/conformer-multilingual-all--gpu-t4' if source_lang != 'english' else 'ai4bharat/whisper--gpu-t4',
        'samplingRate': sampling_rate,
        'preProcessors': [],
        'postProcessors': [],
        'track': False
    }

    resp = requests.post(ASR_ENDPOINT, json = payload)
    status_code = resp.status_code

    if status_code != 200:
        raise APIError(status_code)
    
    resp = resp.json()
    recognized_text = resp['output'][0]['source']

    return recognized_text
