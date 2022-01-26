from nsk import *
from cable_operators import *
from ip_operators import *
import  subprocess

subprocess.Popen(['python3', 'nsk.py'])
subprocess.Popen(['python3', 'cable_operators.py'])
subprocess.Popen(['python3', 'ip_operators.py'])

lines =  (('{}\n'*len(nsk)).format(*nsk)),(('{}\n'*len(cab)).format(*cab)),(('{}\n'*len(ip)).format(*ip))
with open(r"metric", "w") as file:
    for  line in lines:
        file.write(line)

with open("metric", 'r+') as f:
    text = ''.join([line.replace(")", "}")  for line in f.readlines()])
    f.seek(0)
    f.write(text)

with open("metric", 'r+') as f:
    text = ''.join([line.replace("(", "{")  for line in f.readlines()])
    f.seek(0)
    f.write(text)
