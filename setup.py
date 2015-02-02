import os, sys, shutil, time
from shutil import copytree
from distutils.core import setup
setup(name='Karbot',
      version='1.0',
      py_modules=['Karbot', 'ch'],
      )
if os.path.isdir("C:\Kbot") == True:
    shutil.rmtree("C:\Kbot")
copytree(os.getcwd(), 'C:\Kbot')
print "Installed!"
time.sleep(5)
