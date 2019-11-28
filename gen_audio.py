import subprocess
import pandas as pd

data = pd.read_csv("audio_captcha.csv")

for index, line in data.iterrows():
    command = 'aws polly synthesize-speech --output-format "mp3" --voice-id "Joanna" --text "'+line["Cap"]+'" '+ ''.join(line["Cap"].split())+".mp3"
    print(command)
    subprocess.call(command, shell=True)
