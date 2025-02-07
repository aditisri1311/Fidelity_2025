import re
import urllib.request
url = "https://www.redbus.in/info/contactus"
response = urllib.request.urlopen(url)
web_content = response.read().decode('utf-8')

# Regex pattern to extract phone numbers (assumes numbers start with +91 or 6-9)
pattern = r'\+91[-\s]?\d{10}|\b[6-9]\d{9}\b'

# Find all matching phone numbers
phone_numbers = re.findall(pattern, web_content)

print("Extracted Phone Numbers:")
for number in phone_numbers:
    print(number)
