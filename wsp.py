
import os 
import configparser
#Todo:Add  WorksPace
#Todo:Edit WorkSpace
#Todo:Delete WorkSpace
#Todo:Add Actions
#Todo:Edit Actions
#Todo:Delete Actions
import os
from pathlib import Path

path = Path.home()/'.workspace.ini' 

if os.path.isfile(path) != True:
    open(path,'w').close()
    
config = configparser.ConfigParser()
config.read(path)
def add(section,**kwargs):
    if section is not None and kwargs is not None:
        config[section] = kwargs
        with open(path,'w') as configfile:
            config.write(configfile)

def get_list():
    return config.sections()

def get_path(name):
    if name in config.sections():
        return config[name]['path']
    return ""

