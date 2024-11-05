from datetime import datetime
import soundfile

def get_sampling_rate(file_path):
    info = soundfile.info(file_path)
    return info.samplerate

def gen_tts_filename(language):
    curr_date_time = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')   
    return f'TTS_{language}_{curr_date_time}.wav'