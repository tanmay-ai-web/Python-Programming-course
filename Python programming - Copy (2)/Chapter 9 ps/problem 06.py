log_file_path = 'logfile.txt'  # Replace with your log file path

with open(log_file_path, 'r') as file:
    content = file.read()
    if 'python' in content.lower():
        print("'python' found in the log file.")
    else:
        print("'python' not found in the log file.")
