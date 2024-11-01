from constants import *

class LanguageError(Exception):
    def __init__(self, lang_origin, lang):
        # message = f'Invalid {lang_origin} language - "{lang}", please chose from the list below:\n\n{", ".join(LANGUAGES.keys())}'
        message = f'Invalid {lang_origin} language - "{lang}"'
        super().__init__(message)

class DomainError(Exception):
    pass

class VoiceError(Exception):
    def __init__(self, voice):
        message = f'Invalid voice - "{voice}", please chose between "male" or "female"'
        super().__init__(message)