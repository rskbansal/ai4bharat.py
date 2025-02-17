from datetime import datetime
import soundfile

def get_sampling_rate(file_path):
    """Returns the sampling rate of an audio file.

    Arguments:
        file_path (str): Path to the audio file.

    Returns:
        int: The parsed sampling rate.
    """
    info = soundfile.info(file_path)
    return info.samplerate

def gen_tts_filename(language):
    """Generates a filename for the TTS output audio file, incase not provided by the user.

    Arguments:
        language (str): The language of the speech/text.

    Returns:
        str: The generated filename in the format 'TTS_{language}_{current_date_time}.wav'.
    """
    curr_date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')   
    return f'TTS_{language}_{curr_date_time}.wav'