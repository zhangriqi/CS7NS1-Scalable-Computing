import os
from os import path
from pydub import AudioSegment

srcpath = "/Users/zhangruiqi/Downloads/TCD/Modules/CS7NS1SC/Project3/audios"
dstpath = "/Users/zhangruiqi/Downloads/TCD/Modules/CS7NS1SC/Project3/audio_wav/"

def generateWav(source_path, dst_path):
    fileList = os.listdir(source_path)
    # print(fileList[0], fileList[-1])
    print(fileList[100:105])
    for file in fileList[102:104]:
        srcFile = source_path + "/" + file
        print(file)
        sound = AudioSegment.from_file(srcFile)
        dstFile = dst_path + file.strip(".mp3") + ".wav"
        sound.export(dstFile, format = "wav")

generateWav(srcpath, dstpath)