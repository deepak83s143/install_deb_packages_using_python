import os
import time
import sys
import shutil
import subprocess 
from update import install_from_file
# cp_file_src='/etc/passwd'
# cp_file_dest='/home/mademi/UI/'
# _copy=shutil.copy(cp_file_src,cp_file_dest)
# print("passwd file successfully copied to /tmp location")
# time.sleep(2.5)
# file_path='/home/mademi/UI/passwd'
# print("UID of",file_path,"is :- ",os.stat(file_path).st_uid)
# print("GID of",file_path,"is :- ",os.stat(file_path).st_gid)
# time.sleep(2.5)
# os.chown(file_path,1000,1000)

# print("file ownership changed")
# print("UID of",file_path,"is :- ",os.stat(file_path).st_uid)
# print("GID of",file_path,"is :- ",os.stat(file_path).st_gid)

# time.sleep(2.5)
# os.remove(file_path)
# print("File deleted successfully")

# time.sleep(2.5)
try:
    subprocess.check_call([sys.executable,'update.py'],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
except subprocess.CalledProcessError as cpe:
    print(cpe)

