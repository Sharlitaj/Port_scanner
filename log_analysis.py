import pandas as pd
import re

# Function to read the log file
def read_log_file(file_path):
    with open(file_path, "r") as file:
        logs = file.readlines()
    return logs

# Function to parse logs (extracting timestamps and error levels as an example)
def parse_logs(logs):
    log_data = []
    pattern = re.compile(r'(?P<timestamp>\S+\s+\S+)\s+(?P<log_level>\S+)\s+(?P<message>.+)')

    for log in logs:
        match = pattern.match(log)
        if match:
            log_data.append(match.groupdict())
    
    return pd.DataFrame(log_data)

# Main function
def main():
    log_file_path = 'C:/Users/Sharlita/Desktop/CybersecurityProjects/sample_log.log'
    logs = read_log_file(log_file_path)
    parsed_logs = parse_logs(logs) 

    print(parsed_logs.head())  # Display the first few parsed logs

if __name__ == "__main__":
    main()
