import re

text = "A random string. some more random text. Your-Name8_8_8@company.net"

# pattern = re.compile("A random string.")

# pattern = re.compile("[ABC]")

pattern = re.compile("[a-zA-Z0-9\.\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]+")

result = pattern.search(text)

print(result)