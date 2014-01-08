import re
import subprocess
import json

lastLoginCommand = "cat /var/log/auth.log | grep 'sshd.*Accepted' | tail -1"
rawLoginString = subprocess.check_output(lastLoginCommand, shell=True)
ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', rawLoginString)[0] 

if ip[0:7] == "192.168":
    print "Chicago"
else:
    lookupString = "curl -s http://dazzlepod.com/ip/" + ip + ".json"
    lookupResult = subprocess.check_output(lookupString, shell=True)
    jsonResult = json.loads(lookupResult)
    print jsonResult["city"]
