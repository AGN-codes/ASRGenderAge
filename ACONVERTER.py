# ogg2wav converter module
from pydub import AudioSegment

def ogg2wav():
    src = 'new_file.ogg'
    dst = 'new_file.wav'

    sound = AudioSegment.from_ogg(src)
    sound.export(dst, format='wav')