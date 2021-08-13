import os
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
from numpy import mean, power


class recordTrainsColor:

    def __init__(self,rec,cwdOG):

        self.rec=rec
        self.cwdOG = cwdOG
        self.recTrainColor(self.cwdOG, 1)
        self.energyGREEN = self.calcEnergyLedColor(1)
        self.recTrainColor(self.cwdOG, 0)
        self.energyRED = self.calcEnergyLedColor(0)

    def recTrainColor(self, cwdOG, n):
        # function to correct and merge to the needed path
        os.chdir(cwdOG)  # return to original directory in case we moved to wrong directory(after GREEN case)
        cwd = os.getcwd()
        dir = os.path.join(cwd, "Colortrains")
        if not os.path.exists(dir):
            os.mkdir(dir)
        if n == 1:  # if it is a GREEB sound being recorded we go /trains/GREEN
            dir = os.path.join(dir, "GREEN")
        else:  # if it is a RED sound being recorded we go /trains/RED
            dir = os.path.join(dir, "RED")
        if not os.path.exists(dir):
            os.mkdir(dir)
        os.chdir(dir)  # change path to new directory
        cwd = os.getcwd()
        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording


        # if n==1: 
            #pass                     #if it is a GREEN sound record and write in /GREEN/GREEN{i}.wav
        #    for i in range (1,11):
        #    #os.chdir("C:\\Users\\laptop center\\PycharmProjects\\CS\\Colortrains\\GREEN")
        #        print(f'Start saying GREEN for audio #{i}\n')
        #        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        #        sd.wait()  # Wait until recording is finished
        #        write(f'GREEN{i}.wav', fs, myrecording)  # Save as WAV file
        #        data, fsRead = sf.read(f'GREEN{i}.wav')

        # else:                          ##if it is an RED sound record and write in /RED/RED{i}.wav
        #    for i in range (1,6):
        #    #os.chdir("C:\\Users\\laptop center\\PycharmProjects\\CS\\Colortrains\\RED")
        #        print(f'Start saying RED for audio #{i}\n')
        #        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
        #        sd.wait()  # Wait until recording is finished
        #        write(f'RED{i}.wav', fs, myrecording)  # Save as WAV file
        #        data, fsRead = sf.read(f'RED{i}.wav')

    def calcEnergyLedColor(self, n):

        total = 0

        if n == 1:  # if it is an GREEN sound record and write in /GREEN/GREEN{i}.wav
            #os.chdir("C:\\Users\\laptop center\\PycharmProjects\\CS\\Colortrains\\GREEN")
            for i in range(1, 11):
                data, fsRead = sf.read(f'GREEN{i}.wav')  # Extract audio data and sampling rate from file
                result = sum(abs(data) ** 2)  # calculating energy using parseval's theorem
                total += (result.sum())


        else:
            #os.chdir("C:\\Users\\laptop center\\PycharmProjects\\CS\\Colortrains\\RED")
            for i in range(1, 11):
                data, fsRead = sf.read(f'RED{i}.wav')  # Extract audio data and sampling rate from file
                result = sum(abs(data) ** 2)  # calculating energy using parseval's theorem
                total += (result.sum())

        energy = total / 10
        return energy
# r=recordTrainsColor()
# print(r.energyGREEN)
# print(r.energyRED)
