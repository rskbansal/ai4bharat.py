import soundfile 

def get_sampling_rate(file_path):
    info = soundfile.info(file_path)
    return info.samplerate