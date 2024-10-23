BASE_URL = 'https://admin.models.ai4bharat.org'

ASR_ENDPOINT = BASE_URL + '/inference/transcribe'
TRANSLATE_ENDPOINT = BASE_URL + '/inference/translate'
TTS_ENDPOINT = BASE_URL + '/inference/convert'

HEADERS = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
    'Content-Type': 'application/json',
    'Origin': 'https://ai4bharat.iitm.ac.in',
    'Priority': 'u=1, i',
    'Referer': 'https://ai4bharat.iitm.ac.in/',
    'Referrer-Policy': 'strict-origin-when-cross-origin',
    'Sec-CH-UA': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'Sec-CH-UA-Mobile': '?0',
    'Sec-CH-UA-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'cross-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'
}

LANGUAGES = {
    'assamese': {
        'code': 'as',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'bengali': {
        'code': 'bn',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'bodo': {
        'code': 'brx',
        'tts_service': 'ai4bharat/indic-tts-misc--gpu-t4',
    },
    'dogri': {
        'code': 'doi',
        'tts_service': None,
    },
    'english': {
        'code': 'en',
        'tts_service': 'ai4bharat/indic-tts-misc--gpu-t4',
    },
    'gujarati': {
        'code': 'gu',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'hindi': {
        'code': 'hi',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'kannada': {
        'code': 'kn',
        'tts_service': 'ai4bharat/indic-tts-dravidian--gpu-t4',
    },
    'kashmiri': {
        'code': 'ks',
        'tts_service': None,
    },
    'konkani': {
        'code': 'gom',
        'tts_service': None,
    },
    'maithili': {
        'code': 'mai',
        'tts_service': None,
    },
    'malayalam': {
        'code': 'ml',
        'tts_service': 'ai4bharat/indic-tts-dravidian--gpu-t4',
    },
    'manipuri': {
        'code': 'mni',
        'tts_service': 'ai4bharat/indic-tts-misc--gpu-t4',
    },
    'marathi': {
        'code': 'mr',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'meitei': {
        'code': 'mni',
        'tts_service': 'ai4bharat/indic-tts-misc--gpu-t4',
    },
    'nepali': {
        'code': 'ne',
        'tts_service': None,
    },
    'odia': {
        'code': 'or',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'punjabi': {
        'code': 'pa',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'rajasthani': {
        'code': 'raj',
        'tts_service': 'ai4bharat/indic-tts-indo-aryan--gpu-t4',
    },
    'sanskrit': {
        'code': 'sa',
        'tts_service': None,
    },
    'santali': {
        'code': 'sat',
        'tts_service': None,
    },
    'sindhi': {
        'code': 'sd',
        'tts_service': None,
    },
    'tamil': {
        'code': 'ta',
        'tts_service': 'ai4bharat/indic-tts-dravidian--gpu-t4',
    },
    'telugu': {
        'code': 'te',
        'tts_service': 'ai4bharat/indic-tts-dravidian--gpu-t4',
    },
    'urdu': {
        'code': 'ur',
        'tts_service': None,
    }
}