# ref https://pypi.org/project/morse-audio-decoder/

from morse_audio_decoder.morse import MorseCode as morse

code = morse.from_wavfile("./morse_chal.wav")
decoded_code = code.decode()
challange_code ="picoCTF{"+ decoded_code.replace(" ", "_").lower() + "}"
print(challange_code)

