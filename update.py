import subprocess
update=subprocess.check_call(["apt","update"],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# print("update successfully")

def install_from_file(filename="packages"):
    with open(filename,'r') as f:
        package=f.read().splitlines()
    
    for i in package:
        try:
            subprocess.check_call(['apt','install','-y',i],stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(i,"installed successfully")
        except subprocess.CalledProcessError as cpe:
            return cpe
            # print(cpe)
    return install_from_file 

# filename="packages"
install_from_file()


