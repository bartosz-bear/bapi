from pathlib import Path

filename = Path(__file__).resolve().parent.parent.parent.parent.__str__() + "\\requirements.txt"

def drop_builds(x):
    a = '=='.join(x.split('=')[:2])
    return a

# Read requirements.txt and create a list of libraries
with open(filename, 'r') as file:
    lines  = [line.rstrip() for line in file][3:]

# Remove build number
lines = list(map(lambda x: drop_builds(x), lines))

# Save the file
with open(filename, mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(lines))