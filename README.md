# ArduinoSoundProject
The goal of this project is to record and obtain sound data using a board, then have an AI identify when anomalies were recorded. 
Here is a rundown of steps I used and goals I considered:
1. Code the instructions for the board in C++.
2. Put the board together and test it's functionality.
3. Use serial port to read data from board in python.
     - Run the board and collect/ view data.
     - Create and save CSV files with data and timestamps. [CSV example here](examples/csv_format.png). 
     - Create and save graphs using Matplotlib (just for visual help). [Dot plot example here](examples/sound_dot_plot.png).
4. Use Isolation Forest and logic functions to make observations about the data.
     - Use Isolation Forest to detect anomalies in data. Anomalies occur when the sound stays consistent for a while, or when there are sudden fluctuations. 
     - Analyze the data to find the loudest and quietist sound values of the most recent file, as well as a user specified date. All files from the specific date are analyzed and the extremes are returned.

Here is a video showcasing this project running: (video here soon)
# Software and Hardware Used
|Tool|Suggestion|
|-----|----------|
|Python Editor| VS Code (Python 3.13.0)|
|C++ Editor| Arduino IDE 2.3.3|
|AI | Isolation Forest |
|Hardware|Elegoo Mega2560 R3, Sound Sensor|
# Board Diagram
A diagram of my board setup can be found here: [Board Diagram](board_diagram/sound_sensor_board.png).
# Code
All of the code I used can be found in the file titled **code** within the repository, or through the hyperlinks in these descriptions.
1. I first wrote the code for the board in **ArduinoIDE 2.3.3**.
You will need a C++ editor/ interpretor for this. No imports are required. 
The code can be found here: [sound_sensor.ino](code/sound_sensor.ino)

2. Second I wrote the code for saving and using the data from the arduino. I did this using **Python 3.13 in VS Code**. Other python interpreters can be used. Here is a link to the full code: [sound_csv_plot.py](code/sound_csv_plot.py). You will need the following imports:
```
import serial 
import time 
import csv 
import matplotlib.pyplot as plt 
import threading 
import os 
```

3. Lastly I wrote code to make observations on the saved data, utilizing Isolation Forest. I wrote this code using **Python 3.13 in VS Code**. Same as step two, other python interpreters can be used. Here is a link to the full code: [detect_sound_anomaly.py](code/detect_sound_anomaly.py). You will need the following imports:
```
import os
import pandas as pd
import glob
import re
from datetime import datetime
from sklearn.ensemble import IsolationForest
```

