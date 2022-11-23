import re
match = re.match(r"([a-z]+)([0-9]+)", 'foofo21', re.I)
if match:
    items = match.groups()
print(items)