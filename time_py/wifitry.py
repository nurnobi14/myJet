import subprocess
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "All userr profile" in line]

for wifi in wifis:
    result = subprocess.check_output(['netsh','wlan','show','profiles',wifi,'key=clear']).decode('utf-8').split('\n')
    result = [line.split(':')[1][1:-1] for line in result if "key content" in line]
    try:
        print(f'Name: {wifi}, Password: {result[0]}')
    except IndexError:
        print(f'Name {wifi}, Password : can not be read!')