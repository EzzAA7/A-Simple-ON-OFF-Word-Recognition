# pylint: disable=C0321


import os
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
from  recordTrain import recordTrains

#---------------------------------------------Test ON -----------------------------------------
class recordTest(recordTrains):

    def __init__(self):
        self.cwdOG=os.getcwd()
        super(recordTest, self).__init__()
        #self.recordTestOFF(self.cwdOG)
        #self.compareEnergyOFF(self.energyOFF,self.energyON)

        #self.recordTestON(self.cwdOG)
        #self.compareEnergyON(self.energyOFF,self.energyON)

    def recordTestON(self,cwdOG):

        os.chdir(cwdOG)
        cwd=os.getcwd()
        dir = os.path.join(cwd,"tests")
        if not os.path.exists(dir):
            os.mkdir(dir)
        dir = os.path.join(dir,"on")
        if not os.path.exists(dir):
            os.mkdir(dir)   
        os.chdir(dir)
        cwd=os.getcwd()
    def compareEnergyON(self,energyOFF,energyON,i):

        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(f'on{i}.wav', fs, myrecording)  # Save as WAV file     print(f'Audio #{i} ended\n')
        dataOFF, fsOff = sf.read(f'on{i}.wav') 
        resultOFF=sum(abs(dataOFF)**2) 
        energy =(resultOFF.sum())
            

        if(abs(energy-energyON) < abs(energy-energyOFF)):
            return 'ON'
            #print(f'Test file [on] #{i} classified as ON ,E={energy}\n')
        else:
            return 'OFF'
            #print(f'Test file [on] #{i} classified as OFF E={energy}\n')
        


    #------------------------------------------------------------------------
    #-------------TEST off SOUNDS-----------------------------
    def recordTestOFF(self,cwdOG):

        os.chdir(cwdOG)
        cwd=os.getcwd()
        dir = os.path.join(cwd,"tests")
        if not os.path.exists(dir):
            os.mkdir(dir)
        dir = os.path.join(dir,"off")
        if not os.path.exists(dir):
            os.mkdir(dir)
        os.chdir(dir)
        cwd=os.getcwd()

    def compareEnergyOFF(self,energyOFF,energyON,i):

        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording

        #print(f'Start saying off for audio #{i}\n')
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(f'off{i}.wav', fs, myrecording)  # Save as WAV file     print(f'Audio #{i} ended\n')
        dataOFF, fsOff = sf.read(f'off{i}.wav') 
        resultOFF=sum(abs(dataOFF)**2) 
        energy =(resultOFF.sum())


        if(abs(energy-energyON) < abs(energy-energyOFF)):
            return "ON"
            print(f'Test file [off] #{i} classified as ON ,E={energy}\n')
        else:
            return 'OFF'
            #print(f'Test file [off] #{i} classified as OFF E={energy}\n')
            
#-------------------------MAIN FUNC---------------------------------------------------------------------
#r2=recordTest()
