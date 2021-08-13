import os
import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf
from recordTrainColor import recordTrainsColor
from recordTrain import recordTrains
import time

#import RPi.GPIO as GPIO


# ---------------------------------------------Test  -----------------------------------------
class recordTest(recordTrains, recordTrainsColor):

    def __init__(self,rec='rec'):  # intialise function
        self.cwdOG = os.getcwd()  # returns original work dir
        recordTrains.__init__(self)  # and calls its super constructor (recordsTrains and returns their energy)
        recordTrainsColor.__init__(self,rec,self.cwdOG)  # and initialises its super (recordsTrains and returns their energy)


    def recordTest(self, cwdOG, flagStatus):  # function to correct and merge to the needed path

        os.chdir(cwdOG)  # changes directory to original workspace path
        cwd = os.getcwd()  # retrieves current working directory to variable cwd
        dir = os.path.join(cwd, "tests")  # joins current directory with "tests" suffix --> cwd/tests
        if not os.path.exists(dir):  # makes sure file test exists and if it doesnt then make one
            os.mkdir(dir)
        if flagStatus == 'ON':  # if it is an ON sound being recorded
            dir = os.path.join(dir, "on")  # joins current directory with "on" suffix --> cwd/tests/on
        if flagStatus == 'OFF':  # otherwise it is an OFF sound being recorded
            dir = os.path.join(dir, "off")  # joins current directory with "off" suffix --> cwd/tests/off
        if flagStatus == 'GREEN':
            dir = os.path.join(dir, "GREEN")
        if flagStatus == 'RED':
            dir = os.path.join(dir, "RED")
        if not os.path.exists(dir):  # makes sure file(/on or /off) exists and if it doesnt then make one
            os.mkdir(dir)
        os.chdir(dir)  # change path to new directory
        cwd = os.getcwd()  # retrieves current working directory to variable cwd

    def compEnergyLedStatus(self, energyOFF, energyON, i, flagStatus):

        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording

        if flagStatus == 'ON':  # if it is an ON sound record and write in /on/on{i}.wav
            #            os.chdir("//home/pi/Desktop//trains//on")
            print(f'Start saying on for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()  # Wait until recording is finished
            write(f'on{i}.wav', fs, myrecording)  # Save as WAV file
            data, fsRead = sf.read(f'on{i}.wav')

        if flagStatus == 'OFF':  ##if it is an OFF sound record and write in /off/off{i}.wav
            # os.chdir("//home/pi/Desktop//trains//off")
            print(f'Start saying off for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()  # Wait until recording is finished
            write(f'off{i}.wav', fs, myrecording)  # Save as WAV file
            data, fsRead = sf.read(f'off{i}.wav')

        result = sum(abs(data) ** 2)  # calculating energy using parseval's theorem
        energy = (result.sum())

        if (abs(energy - energyON) < abs(
                energy - energyOFF)):  # we compare energy with avgEnergy to determine if its ON or OFF sound
            print(f'Test file #{i} classified as ON ,E={energy}\n')
            print("LED on \n")
            print("******************************")
            #GPIO.output(18, GPIO.HIGH)
            time.sleep(1)
        else:
            print(f'Test file #{i} classified as OFF ,E={energy}\n')
            print("LED off \n")
            print("******************************")
           # GPIO.output(18, GPIO.LOW)



    def compEnergyLedColor(self, energyGREEN, energyRED, i, flagStatus):

        fs = 44100  # Sample rate
        seconds = 2  # Duration of recording
        if flagStatus == 'GREEN':
            print(f'Start saying green for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()  # Wait until recording is finished
            write(f'green{i}.wav', fs, myrecording)  # Save as WAV file
            data, fsRead = sf.read(f'GREEN{i}.wav')
        if flagStatus == 'RED':
            print(f'Start saying red for audio #{i}\n')
            myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
            sd.wait()  # Wait until recording is finished
            write(f'red{i}.wav', fs, myrecording)  # Save as WAV file
            data, fsRead = sf.read(f'RED{i}.wav')
            
        result = sum(abs(data) ** 2)  # calculating energy using parseval's theorem
        energy = (result.sum())

        if (abs(energy - energyGREEN) < abs(energy - energyRED)):  # we compare energy with avgEnergy to determine if its ON or OFF sound
            print(f'Test file #{i} classified as GREEN ,E={energy}\n')
            print("LED GREEN \n")
            print("******************************")
        else:
            print(f'Test file #{i} classified as RED ,E={energy}\n')
            print("LED RED \n")
            print("******************************")
# -------------------------MAIN FUNC---------------------------------------------------------------------
def main():
   # GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(18, GPIO.OUT)
    print("Command the LED")
    r2 = recordTest()
    # print(r2.energyOFF)
    # print(r2.energyON)
    iOff = 0  # iOff refers to the number of the sound ie: off1 when on{iOff=1}
    iOn = 0  # iOn refers to the number of the sound ie: on2 when on{iOn=2}
    iRed = 0
    iGreen = 0
    flagStatus = ''  # flag is NONE for OFF sound, and its TRUE for ON sounds to differtiate between them

    while (1):

        ans = input("Please determine the LED color you want to control green/red \n")
        # check input if its on or off to recordTest then compare its results

        if ans == 'green':
            flagStatus = 'GREEN'
            r2.recordTest(r2.cwdOG, flagStatus)
            r2.compEnergyLedColor(r2.energyGREEN, r2.energyRED, iGreen, flagStatus)
            iGreen = iGreen + 1
            ans2 = input("Now determine the status desired on/off\n")
            if ans2 == 'on':
                flagStatus = 'ON'
                r2.recordTest(r2.cwdOG, flagStatus)
                r2.compEnergyLedStatus(r2.energyOFF, r2.energyON, iOn, flagStatus)
                iOn = iOn + 1

            elif ans2 == 'off':
                flagStatus = 'OFF'
                r2.recordTest(r2.cwdOG, flagStatus)
                r2.compEnergyLedStatus(r2.energyOFF, r2.energyON, iOff, flagStatus)
                iOff = iOff + 1

        elif ans == 'red':
            flagStatus = 'RED'
            r2.recordTest(r2.cwdOG, flagStatus)
            r2.compEnergyLedColor(r2.energyGREEN, r2.energyRED, iRed, flagStatus)
            iRed = iRed + 1
            ans2 = input("Now determine the status desired on/off\n")
            if ans2 == 'on':
                flagStatus = 'ON'
                r2.recordTest(r2.cwdOG, flagStatus)
                r2.compEnergyLedStatus(r2.energyOFF, r2.energyON, iOn, flagStatus)
                iOn = iOn + 1

            elif ans2 == 'off':
                flagStatus = 'OFF'
                r2.recordTest(r2.cwdOG, flagStatus)
                r2.compEnergyLedStatus(r2.energyOFF, r2.energyON, iOff, flagStatus)
                iOff = iOff + 1
        else:
            exit()


if __name__ == "__main__":
    # GPIO.output(18,GPIO.LOW)
    main()