import os
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf

class recordTrains:

    def __init__(self):
        
        self.cwdOG=os.getcwd()
        self.recordTrainON()
        self.energyON = self.calculateEnergyON()

        self.recordTrainOFF(self.cwdOG)
        self.energyOFF=self.calculateEnergyOFF()
        #print(self.energyOFF)



    def recordTrainON(self):

        cwd=os.getcwd()
        dir = os.path.join(cwd,"trains")
        if not os.path.exists(dir):
            os.mkdir(dir)
        dir = os.path.join(dir,"on")
        if not os.path.exists(dir):
            os.mkdir(dir)
            
        os.chdir(dir)
        cwd=os.getcwd()

        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording

        #recObj = audiorecorder(44000, 24, 1);% record at Fs=44khz, 24 bits per sample
        """ for i in range (1,11):
            print(f'Start saying ON for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            write(f'on{i}.wav', fs, myrecording)  # Save as WAV file     print(f'Audio #{i} ended\n')

        """
    def calculateEnergyON(self):

        totalON = 0
        for i in range(1,9):
            dataON, fsON = sf.read(f'on{i}.wav') 
            resultON=sum(abs(dataON)**2) 
            totalON +=(resultON.sum())

        energyON=totalON/8
        return energyON

#------------------------------------------------------------------------
#-------------FOR THE OFF SOUNDS-----------------------------
    def recordTrainOFF(self,cwdOG):

        os.chdir(cwdOG)
        cwd=os.getcwd()
        dir = os.path.join(cwd,"trains")
        if not os.path.exists(dir):
            os.mkdir(dir)
        dir = os.path.join(dir,"off")
        if not os.path.exists(dir):
            os.mkdir(dir)

        os.chdir(dir)
        cwd=os.getcwd()

        """ for i in range (1,5):
            print(f'Start saying OFF for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            write(f'off{i}.wav', fs, myrecording)  # Save as WAV file     print(f'Audio #{i} ended\n')
        """
    # Extract audio data and sampling rate from file 
    def calculateEnergyOFF(self):
        totalOFF = 0

        for i in range(1,5):
            dataOFF, fsOff = sf.read(f'off{i}.wav') 
            resultOFF=sum(abs(dataOFF)**2) 
            totalOFF +=(resultOFF.sum())

        energyOFF=totalOFF/4
        return energyOFF

    def getEnergyON(self):
        return self.energyON

    def getEnergyOFF(self):
        return self.energyOFF

#r1=recordTrains()
#print(r1.energyON)