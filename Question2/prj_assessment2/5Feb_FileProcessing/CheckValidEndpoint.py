import re
# Open the file
with open("C:/DBMS/Valid_endpoint.txt", "r") as file:
    lines = file.readlines()

# ReEx to match the valid endpoint format
pattern = r'^https://fidelity//rest//v\d+\.\d+\.\d+$'

# Checking each line in the file
for line in lines:
    line = line.strip()  # Remove trailing
    if re.match(pattern, line):
        print(f"Valid Endpoint: {line}")
    else:
        print(f"Invalid Endpoint: {line}")
