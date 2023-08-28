import re
from glob import glob

for filepath in glob("Logs/Logs/*.xml"):
    text = re.sub('<[^<]+>', "", open(filepath, encoding="mbcs").read())
    with open("output.txt", "a", encoding="mbcs") as f:
        f.write(text[:7] + "\n")