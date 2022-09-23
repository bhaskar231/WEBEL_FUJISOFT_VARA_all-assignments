import re

text = input("Enter a String: ")
pattern =input("Enter a pattern String: ")

for match in re.findall(pattern, text):
    print('Found "%s"' % match)