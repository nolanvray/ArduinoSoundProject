# ArduinoSoundProject
The goal of this project is to record and obtain sound data using a board, then have an AI identify when extreme sounds (highs and lows) were recorded. 
Here is a rundown of steps I used and goals I considered:
1. Code the instructions for the board.
2. Put the board together and test it's functionality.
3. Use serial port to read data from board in python.
     - Run the board and collect/ view data.
     - Create and save CSV files with data and timestamps. 
     - Create and save graphs using Matplotlib.
4. Find an open-source AI model to use. Edit it to fit the projects needs.
     - Answer questions relating to max and min sounds.

# Software and Hardware Used
|Tool|Suggestion|
|-----|----------|
|Python Editor| VS Code (Python 3.13.0)|
|C++ Editor| Arduino IDE 2.3.3|
|AI | GoogleCollab |
|Hardware|Elegoo Mega2560 R3, Sound Sensor|
# Board Diagram
A diagram of my board setup can be found here: [Board Diagram](ArduinoSoundProject/board diagram/ ArduinoSoundSensor.png)
# Code
1. I first wrote the code for the board in **ArduinoIDE 2.3.3**.
There are no imports needed, just a C++ interpreter.
The code can be found here: [SoundSensor.ino](code/SoundSensor.ino)
3. Second I wrote the code for saving and using the data from the arduino. I did this using **Python 3.13 in VS Code**. Other python interpreters can be used as long as they support the following imports:
```
import serial 
import time 
import csv 
import matplotlib.pyplot as plt 
import threading 
import os 
```
Here is a link to the full code, which can also be found in the file titled <ins>code</ins> within the repository: [ArduinoSoundReadings.py](code/ArduinoSoundReadings.py)

