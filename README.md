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
[ArduinoSoundSensor](https://github.com/user-attachments/assets/e8b21ab5-88b1-4c74-9703-ec576d1e6b37)

