from pygame import mixer
import os
from google.cloud import texttospeech
import random

# Instantiates a client
client = texttospeech.TextToSpeechClient()

# Set the text input to be synthesized
def speak(text1,l):
    #import shutil
    #shutil.rmtree('voices/') 

    synthesis_input = texttospeech.types.SynthesisInput(text=text1)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='en-US',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    filename=random.randint(1,10000000)
    # The response's audio_content is binary.
    with open(str(filename)+'output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        
        print('Audio content written to file "output.mp3"')
    file = str(filename)+'output.mp3'
    mixer.init()
    a=mixer.music.load(file)
    #print(a.length())
    if(l==''):
        pass
    else:
        os.remove(l)
    
    mixer.music.play()
    
    return file
def speakhindi(text1,l):
    #import shutil
    #shutil.rmtree('voices/') 

    synthesis_input = texttospeech.types.SynthesisInput(text=text1)

    # Build the voice request, select the language code ("en-US") and the ssml
    # voice gender ("neutral")
    voice = texttospeech.types.VoiceSelectionParams(
        language_code='hi-IN',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

    # Select the type of audio file you want returned
    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3)

    # Perform the text-to-speech request on the text input with the selected
    # voice parameters and audio file type
    response = client.synthesize_speech(synthesis_input, voice, audio_config)
    filename=random.randint(1,10000000)
    # The response's audio_content is binary.
    with open(str(filename)+'output.mp3', 'wb') as out:
        # Write the response to the output file.
        out.write(response.audio_content)
        
        print('Audio content written to file "output.mp3"')
    file = str(filename)+'output.mp3'
    mixer.init()
    a=mixer.music.load(file)
    #print(a.length())
    if(l==''):
        pass
    else:
        os.remove(l)
    
    mixer.music.play()
    
    return file

        
        
