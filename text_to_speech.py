import speech_recognition as sr
import pyttsx3 as tts

def speech_to_mp3():
    # file must be within scope
    mp3FileName = 'filename'
    
    engine = tts.init()
    
    
    engine.save_to_file("enter  your text  here",mp3FileName)
    engine.runAndWait()
    
    return mp3FileName

# Reading the mp3 file
engine = sr.Recognizer()
mp3FileName = speech_to_mp3()

with sr.AudioFile(mp3FileName) as source:
    print("File is being analyzed...")
    audio = engine.record(source)
    
# Extracting and printing as text
try:
    text = engine.recognize_google(audio)
    print(f'Text: {text}')
    txtFile = open('ConvertedMP3.txt', 'w')
    txtFile.write(text)
except Exception as e:
    print(f'Error: {e}')
    