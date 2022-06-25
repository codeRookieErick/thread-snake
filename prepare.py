import os
from typing import Dict, List

def clean_old_dist():
    os.system('rd /S /Q dist')

def get_local(directory:str):
    return os.path.join(os.path.dirname(__file__), directory)

def create_from_template(source:str, target:str, params:Dict[str, str]):
    data = ''
    with open(get_local(os.path.join('templates', source)), 'r', encoding = 'latin1') as r:
        data = r.read()
    for k in params:
        data = data.replace(f"[{k}]", params[k])
    with open(get_local(target), 'w', encoding = 'latin1') as r:
         r.write(data)

def increment_version(versionFile:str = 'version.txt'):
    versionData:List[str] = []
    with open(versionFile, 'r', encoding='latin1') as f:
        versionData = f.read().split('.')
    versionData[2] = str(int(versionData[2]) + 1)
    version = '.'.join(versionData)
    with open(versionFile, 'w', encoding='latin1') as f:
        f.write(version)
    print(f'Version set to : {version}')
    return version

params = {}
params["version"] = increment_version()
clean_old_dist()
create_from_template("README.txt", "README.md", params)
create_from_template("setup.txt", "setup.py", params)
create_from_template("install.txt", "install.bat", params)