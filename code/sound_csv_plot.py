'''
Written by Nolan Ray (https://github.com/nolanvray) for a school project.
Last updated on 12/04/24.

This code collects sound data from an arduino device and then uses said data to create
a csv file and dot plot.

Creates a new file each time it is run.
Type 'stop' and press enter to save data and end the program.
'''
import serial # For serial connection
import time # For timestamp creation
import csv # For creating csv files
import matplotlib.pyplot as plt # For plot creation
import threading # For easier reception of user input
import os # For checking file paths


stopCollection = False

# Function for checking input (non-blocking)
# If user types in 'stop' and presses enter, data will save and collection ends
def checkInput():
     global stopCollection
     while not stopCollection:
         user_input = input()
         if user_input.lower() == 'stop': 
              stopCollection = True
              print("Collection ended, data saved.")

# Opening serial port. In my case COM3 or /dev/ttyS2
ser = serial.Serial('COM3',9600)
time.sleep(2) #wait for connection  


# Start a thread for user input, so that typing is not interrputed by any data output/ messages
input_thread = threading.Thread(target=checkInput)
input_thread.daemon = True  # Daemonize thread so it stops with the program
input_thread.start()      


data_list = []
stopCollection = False #flag to stop data collection

print("Collecting data...")
print("Type 'stop' to end collection:")


# Collecting data
while not stopCollection:
        if ser.in_waiting > 0:
            
            line = ser.readline().decode('utf-8').rstrip()
            
            #Debugging line, comment out when not needed:
            #print(f"Data: {line}") 
           
           #Time
            current_time = time. strftime("%Y-%m-%d %H:%M:%S")
           
            #Add time and sound to data list
            data_list.append([current_time, line])
            

        time.sleep(1)
        
ser.close() #close serial port

# Create Unique filename based on date
date_str= time.strftime("%Y-%m-%d")
sequence_number = 1

# Check where in sequence you are on date of collection
# Put in the filepath where your csv files are stored
while os.path.exists('Your filepath here'):
    sequence_number += 1

# Name for file
file_path =f'Your Filepath\\data_{date_str}_{sequence_number:02d}.csv'


'''
Writes the CSV file in the format below.

|Timestamp|Sound Value(D)|
--------------------------
|2024-11-19 23:26:23| 235|
|2024-11-19 23:26:24|234|

'''
with open(file_path, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Timestamp','Sound Value(D)'])
    writer.writerows(data_list)

#Prepare for plotting
sound_values = [float (row[1]) for row in data_list] #Convert to float for plotting
x_values = list(range(len(sound_values))) #Creating x values

#Create line plot
plt.figure(figsize=(10,5))
plt.plot(x_values, sound_values, marker='o', linestyle='-',color='b' )
plt.title('Sound Readings') # Plot title
plt.xlabel('Time Recorded')# X axis label
plt.ylabel('Sound Value (D)')# Y axis label
plt.grid(True)

# Plot management
plt.savefig(f'Your Filepath\\sound_values_plot_{date_str}_{sequence_number:02d}.png') #Save plot
plt.show() #Show Plot



