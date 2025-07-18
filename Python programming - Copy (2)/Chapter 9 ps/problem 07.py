''' Write a program to find out the line number where python is present from ques 6.'''  


log_file_path = 'logfile.txt'  
with open(log_file_path, 'r') as file:
    lines = file.readlines()
    def find_python_line(lines):
        for line_number, line in enumerate(lines, start=1):
            if 'python' in line.lower():
                print(f"'python' found in line {line_number}.")
        return line_number
        
    find_python_line(lines)