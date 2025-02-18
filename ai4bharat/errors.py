from .constants import *

class LanguageError(Exception):
    def __init__(self, lang_origin, lang):
        # message = f'Invalid {lang_origin} language - "{lang}", please chose from the list below:\n\n{", ".join(LANGUAGES.keys())}'
        message = f'Invalid {lang_origin} language - "{lang}"'
        super().__init__(message)

class DomainError(Exception):
    def __init__(self, domain):
        message = f'Invalid domain - "{domain}"'
        super().__init__(message)

class VoiceError(Exception):
    def __init__(self, voice):
        message = f'Invalid voice - "{voice}", please chose between "male" or "female"'
        super().__init__(message)

class APIError(Exception):
    def __init__(self, status_code):
        message = f'An error occured, API returned status code - {status_code}'
        super().__init__(message)

class AudioError(Exception):
    def __init__(self, sampling_rate):
        message = f'Invalid sampling rate - {sampling_rate}, must be atleast 8000 for clear audio'
        super().__init__(message)