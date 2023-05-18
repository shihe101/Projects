import os
import subprocess

# OS works with the operating system 
# Subprocess execute system commands

# Define the path to the log file
log_file = "malicious_activity.log" # where suspicious activity will be logged

# Define a list of suspicious keywords
suspicious_keywords = ["malware", "virus", "backdoor", "exploit", "rootkit"]

# Function to search for suspicious keywords in a file
def search_keywords(file_path):
  #  takes a file path as input 
  # searches for suspicious keywords in the file's content
    with open(file_path, "r") as file:
        content = file.read()
        for keyword in suspicious_keywords:
            if keyword in content:
                return True
    return False

# Function to scan a directory for suspicious files
# Takes a directory path as input 
# Scans the directory for suspicious files

def scan_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if search_keywords(file_path):
                log_suspicious_activity(file_path)

# Function to log suspicious activity to a file
# File path as input
# Logs the suspicious activity to the log file

def log_suspicious_activity(file_path):
    with open(log_file, "a") as file:
        file.write("Suspicious activity detected: {}\n".format(file_path))

# Main function to start the monitoring process
# Takes a target directory as input 
# Continuously monitors the system
def monitor_system(directory):
    while True:
        scan_directory(directory)

# Example usage
if __name__ == "__main__":
    target_directory = "/path/to/directory"
    monitor_system(target_directory)


#  Python script that can be used to monitor a system for malicious activity
#  This is practical script and may need to be customized 
