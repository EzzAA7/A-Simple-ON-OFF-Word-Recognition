import os
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
from numpy import mean, power


class recordTrains:

    def __init__(self):

        self.cwdOG = os.getcwd()
        self.recTrains(self.cwdOG, 1)
        self.energyON = self.calcEnergyLedStatus(1)
        self.recTrains(self.cwdOG, 0)
        self.energyOFF = self.calcEnergyLedStatus(0)

    def recTrains(self, cwdOG, n):
        # function to correct and merge to the needed path
        if n == 0:
            os.chdir(cwdOG)  # return to original directory in case we moved to wrong directory(after ON case)
        cwd = os.getcwd()
        dir = os.path.join(cwd, "trains")
        if not os.path.exists(dir):
            os.mkdir(dir)
        if n == 1:  # if it is an ON sound being recorded we go /trains/on
            dir = os.path.join(dir, "on")
        else:  # if it is an OFF sound being recorded we go /trains/off
            dir = os.path.join(dir, "off")
        if not os.path.exists(dir):
            os.mkdir(dir)
        os.chdir(dir)  # change path to new directory
        cwd = os.getcwd()
        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording


        #if n==1:                      #if it is an ON sound record and write in /on/on{i}.wav
         #   for i in range (1,11):
          #      print(f'Start saying on for audio #{i}\n')
           #     myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            #    sd.wait()  # Wait until recording is finished
             #   write(f'on{i}.wav', fs, myrecording)  # Save as WAV file
              #  data, fsRead = sf.read(f'on{i}.wav')

       # else:                          ##if it is an OFF sound record and write in /off/off{i}.wav
        #    for i in range (1,11):
         #       print(f'Start saying off for audio #{i}\n')
          #      myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
           #     sd.wait()  # Wait until recording is finished
            #    write(f'off{i}.wav', fs, myrecording)  # Save as WAV file
             #   data, fsRead = sf.read(f'off{i}.wav')

    def calcEnergyLedStatus(self, n):

        total = 0
        if n == 1:  # if it is an ON sound record and write in /on/on{i}.wav
            for i in range(1, 11):
                #os.chdir("C:\\Users\\laptop center\\PycharmProjects\\CS\\trains\\on")
                data, fsRead = sf.read(f'on{i}.wav')  # Extract audio data and sampling rate from file
                result = sum(abs(data) ** 2)  # calculating energy using parseval's theorem
                total += (result.sum())
        else:
            for i in range(1, 11):
                #os.chdir("C:\\Users\\laptop center\\PycharmProjects\\CS\\trains\\off")
                data, fsRead = sf.read(f'off{i}.wav')  # Extract audio data and sampling rate from file
                result = sum(abs(data) ** 2)  # calculating energy using parseval's theorem
                total += (result.sum())

        energy = total / 10
        return energy