# A-Simple-ON-OFF-Word-Recognition
The aim of this project is to build a hardware system by which a LED can be controlled by voice. When you say a a
word “ON” the LED should be turned on, and when you say a word “OFF” the LED should be turned off. In order to
simplify the project and help you manage the project development, we divide it into two phases, as follow.

Part I: Building a simple ON/OFF word recognition 

In this phase, you need to develop and test a system (application) that can recognize the spoken ‘ON’ and
spoken ‘OFF’. To do this, you need to have few samples of recorded ON and OFF (each in separate .wav
file and of the same sampling frequency). To make it gender independent, it is better to have a mix of
male and female speech.
In order to distinguish ON from OFF, it is necessary to find a feature that can be computed on an unknown
signal whose value is usually small for on and large for off (or vice versa). The power spectral density,
which is based on the FFT, is a plot of the estimated spectrum of a signal. If the power spectral density of
a recording of a person saying ‘on’ is compared to that of ‘off’, usually the spectrum of ‘off’ has more
energy in the high frequencies because of the “f” sound in off.
In addition to these spectral features of the two words (on/off), you also can use energy and zero-crossing

rate of the two signals. ‘off’ has /f/ sound dominant which has less energy and high frequency (high zero-
crossings) compared to the ‘on’ which has /o/ sound (vowel) dominant.

Part II: Hardware Implementation

In this phase, you need to develop a hardware system (we recommend to use Raspberry Pi) with a LED
and a microphone. You need to run your ON/OFF system in Part I on the Raspberry PI and control the LED
as described earlier. You need to test your system carefully and report the accuracy in your report.
You need to demonstrate your working system to your instructor or TA for project evaluation.

Part III: Controlling Red and Green LEDs

In this part, you have to extend your system and make it able to control two LEDs (red and green), instead
of one, by voice. In order to turn the red LED one, you say a word ‘red’ followed by a word ‘on’, where to
turn it off you just say ‘red’ followed by ‘off’. The same thing for the green LED.
This system should be run on your hardware system, similar to your system in part II above.
