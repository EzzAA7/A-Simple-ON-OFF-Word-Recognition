# pylint: disable=C0321
import os
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
from  recordTrain import recordTrains
import time
# import RPi.GPIO as GPIO

#---------------------------------------------Test  -----------------------------------------
class recordTest(recordTrains):

    def __init__(self):                 #intialise function  
        self.cwdOG=os.getcwd()          #returns original work dir
        super(recordTest, self).__init__()  #and initialises its super (recordsTrains and returns their energy)

    def recordTest(self,cwdOG,flagStatus):  #function to correct and merge to the needed path

        os.chdir(cwdOG)                     #changes directory to original workspace path                 
        cwd=os.getcwd()                     #retrieves current working directory to variable cwd
        dir = os.path.join(cwd,"tests")     #joins current directory with "tests" suffix --> cwd/tests
        if not os.path.exists(dir):         #makes sure file test exists and if it doesnt then make one
            os.mkdir(dir)
        if flagStatus==True:                #if it is an ON sound being recorded 
            dir = os.path.join(dir,"on")    #joins current directory with "on" suffix --> cwd/tests/on
        else:                               #otherwise it is an OFF sound being recorded 
            dir = os.path.join(dir,"off")   #joins current directory with "off" suffix --> cwd/tests/off  
        if not os.path.exists(dir):         #makes sure file(/on or /off) exists and if it doesnt then make one
            os.mkdir(dir)   
        os.chdir(dir)                       #change path to new directory
        cwd=os.getcwd()                     #retrieves current working directory to variable cwd

    def compEnergyLedStatus(self,energyOFF,energyON,i,flagStatus):

        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording
        
        if flagStatus==True:             #if it is an ON sound record and write in /on/on{i}.wav

            print(f'Start saying on for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
            sd.wait()  # Wait until recording is finished
            write(f'on{i}.wav', fs, myrecording)  # Save as WAV file     
            data, fsRead = sf.read(f'on{i}.wav') 

        else:                           ##if it is an OFF sound record and write in /off/off{i}.wav                 
            print(f'Start saying off for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()  # Wait until recording is finished
            write(f'off{i}.wav', fs, myrecording)  # Save as WAV file     
            data, fsRead = sf.read(f'off{i}.wav')

        result=sum(abs(data)**2) #calculating energy using parseval's theorem
        energy =(result.sum())
            
        if(abs(energy-energyON) < abs(energy-energyOFF)): #we compare energy with avgEnergy to determine if its ON or OFF sound
            print(f'Test file #{i} classified as ON ,E={energy}\n')
            print("LED on \n")
            print("******************************")
            # GPIO.output(18,GPIO.HIGH)
            time.sleep(1)
        else:
            print(f'Test file #{i} classified as OFF ,E={energy}\n')
            print("LED off \n")
            print("******************************")
            # GPIO.output(18,GPIO.LOW)
        
#-------------------------MAIN FUNC---------------------------------------------------------------------
def main():
    # GPIO.setmode(GPIO.BCM)
    # GPIO.setwarnings(False)
    # GPIO.setup(18,GPIO.OUT)
    print("Command the LED")

    r2=recordTest()
    print(r2.energyOFF)
    print(r2.energyON)
    iOff=0                      #iOff refers to the number of the sound ie: off1 when on{iOff=1}
    iOn=0                       #iOn refers to the number of the sound ie: on2 when on{iOn=2}
    flagStatus=None             #flag is NONE for OFF sound, and its TRUE for ON sounds to differtiate between them

    while(1):

        ans= input("Please Press 'on' or 'off' to record on/off sound test and compare \n")
        #check input if its on or off to recordTest then compare its results
        if ans=='on':
            flagStatus= True
            r2.recordTest(r2.cwdOG,flagStatus)
            r2.compEnergyLedStatus(r2.energyOFF,r2.energyON,iOn,flagStatus)
            iOn=iOn+1           

        elif ans=='off':
            flagStatus=None
            r2.recordTest(r2.cwdOG,flagStatus)
            r2.compEnergyLedStatus(r2.energyOFF,r2.energyON,iOff,flagStatus)
            iOff=iOff+1

        else :
            exit()

if __name__== "__main__":
    main()