import os
import pandas as pd
import glob
import re
from datetime import datetime
from sklearn.ensemble import IsolationForest

# Function to find the most recent CSV file based on the date in the filename
def find_latest_csv(directory):
    csv_files = glob.glob(os.path.join(directory, "data_*.csv"))
    latest_file = None
    latest_datetime = None

    for file in csv_files:
        match = re.search(r"data_(\d{4}-\d{2}-\d{2}_\d{2})\.csv", file)
        if match:
            datetime_str = match.group(1)
            datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d_%H")

            if latest_datetime is None or datetime_obj > latest_datetime:
                latest_datetime = datetime_obj
                latest_file = file

    return latest_file

# Function to handle user input for a date, accepting different formats
def parse_date_input(date_input):
    date_formats = ["%Y-%m-%d", "%m-%d-%Y"]

    for date_format in date_formats:
        try:
            return datetime.strptime(date_input, date_format).strftime("%Y-%m-%d")
        except ValueError:
            continue

    raise ValueError("Date format not recognized. Please enter a valid date in YYYY-MM-DD or MM-DD-YYYY format.")

# Function to find the loudest and quietest sounds for a specific date
def find_loudest_and_quietest_on_date(directory, target_date_str):
    target_date = datetime.strptime(target_date_str, "%Y-%m-%d").date()
    csv_files = glob.glob(os.path.join(directory, f"data_{target_date_str}_*.csv"))

    if not csv_files:
        print(f"No files found for the date: {target_date_str}")
        return None

    overall_loudest_value = -float('inf')
    overall_quietest_value = float('inf')
    overall_loudest_timestamp = ''
    overall_quietest_timestamp = ''
    overall_loudest_filename = ''
    overall_quietest_filename = ''

    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        df['Timestamp'] = df['Timestamp'].astype(str)
        df['Sound Value(D)'] = df['Sound Value(D)'].astype(float)
        df = df.fillna('')

        loudest_row = df.loc[df['Sound Value(D)'].idxmax()]
        quietest_row = df.loc[df['Sound Value(D)'].idxmin()]

        if loudest_row['Sound Value(D)'] > overall_loudest_value:
            overall_loudest_value = loudest_row['Sound Value(D)']
            overall_loudest_timestamp = loudest_row['Timestamp']
            overall_loudest_filename = os.path.basename(csv_file)

        if quietest_row['Sound Value(D)'] < overall_quietest_value:
            overall_quietest_value = quietest_row['Sound Value(D)']
            overall_quietest_timestamp = quietest_row['Timestamp']
            overall_quietest_filename = os.path.basename(csv_file)

    loudest_time = overall_loudest_timestamp.split(" ")[1]
    quietest_time = overall_quietest_timestamp.split(" ")[1]

    print(f"\nOn {target_date_str}, the loudest sound was {overall_loudest_value} at {loudest_time} in file: {overall_loudest_filename}")
    print(f"On {target_date_str}, the quietest sound was {overall_quietest_value} at {quietest_time} in file: {overall_quietest_filename}")

    return overall_loudest_value, overall_loudest_timestamp, overall_loudest_filename, overall_quietest_value, overall_quietest_timestamp, overall_quietest_filename

# Function to detect anomalies using Isolation Forest
def detect_anomalies_isolation_forest(df, contamination=0.05):
    # Assuming Sound Value(D) is the feature to detect anomalies
    X = df[['Sound Value(D)']]

    # Create an IsolationForest model
    model = IsolationForest(contamination=contamination)

    # Fit the model and predict anomalies (1 for normal, -1 for anomaly)
    df['Anomaly'] = model.fit_predict(X)

    # Filter out the anomalies (-1 indicates anomaly)
    anomalies = df[df['Anomaly'] == -1]

    if anomalies.empty:
        return None
    else:
        return anomalies[['Timestamp', 'Sound Value(D)']]

# --- Main Execution ---
def main():
    csv_directory = r"C:\Users\sl0th\Arduino_Data"

    # Get user input for a specific date and analyze that date's data
    while True:
        target_date_str = input("Enter a date (YYYY-MM-DD) to find loudest and quietest sounds for that day: ")
        try:
            # Attempt to parse and validate the date
            target_date_str = parse_date_input(target_date_str)
            print(f"Searching for files for date: {target_date_str}")
            
            # Find loudest and quietest for the given date
            loudest_quietest_info = find_loudest_and_quietest_on_date(csv_directory, target_date_str)

            # Now, we need to check for anomalies for that date using Isolation Forest
            csv_files = glob.glob(os.path.join(csv_directory, f"data_{target_date_str}_*.csv"))
            all_anomalies = []

            for csv_file in csv_files:
                df = pd.read_csv(csv_file)
                df['Timestamp'] = df['Timestamp'].astype(str)
                df['Sound Value(D)'] = df['Sound Value(D)'].astype(float)
                df = df.fillna('')

                anomalies = detect_anomalies_isolation_forest(df)
                if anomalies is not None:
                    all_anomalies.append(anomalies)
                    print(f"\nAnomalies in {os.path.basename(csv_file)}:")
                    print(anomalies)

            if not all_anomalies:
                print("\nNo anomalies detected for this date.")
            
            # Display info for the most recent file
            latest_csv_file = find_latest_csv(csv_directory)
            latest_df = pd.read_csv(latest_csv_file)
            latest_df['Timestamp'] = latest_df['Timestamp'].astype(str)
            latest_df['Sound Value(D)'] = latest_df['Sound Value(D)'].astype(float)

            loudest_row = latest_df.loc[latest_df['Sound Value(D)'].idxmax()]
            quietest_row = latest_df.loc[latest_df['Sound Value(D)'].idxmin()]

            loudest_time = loudest_row['Timestamp'].split(" ")[1]
            quietest_time = quietest_row['Timestamp'].split(" ")[1]

            print(f"\nIn the most recent file ({os.path.basename(latest_csv_file)}), the loudest sound was {loudest_row['Sound Value(D)']} at {loudest_time}")
            print(f"In the most recent file, the quietest sound was {quietest_row['Sound Value(D)']} at {quietest_time}")
            
            break  # Exit the loop once a valid date is entered
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD or MM-DD-YYYY.")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()