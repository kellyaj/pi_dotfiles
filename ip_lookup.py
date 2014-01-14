import re
import subprocess
import json

class Governor(object):

    @staticmethod
    def run_command(command_string):
        return subprocess.check_output(command_string, shell=True)

    @staticmethod
    def parse_ip(raw_ip_string):
        return re.findall( r'[0-9]+(?:\.[0-9]+){3}', raw_ip_string)[0]

    @staticmethod
    def lookup(ip):
        if ip[0:7] == "192.168":
            return "Home"
        else:
            lookup_string = "curl -s http://dazzlepod.com/ip/" + ip + ".json"
            lookup_result = Governor.run_command(lookup_string)
            json_result = json.loads(lookup_result)
            return json_result["city"]

login_1 = "cat /var/log/auth.log | grep 'sshd.*Accepted' | tail -2 | head -1"
login_2 = "cat /var/log/auth.log | grep 'sshd.*Accepted' | tail -3 | head -1"
login_3 = "cat /var/log/auth.log | grep 'sshd.*Accepted' | tail -4 | head -1"

commands = [login_1, login_2, login_3]

locations = []

for idx, command in enumerate(commands):
    ip = Governor.parse_ip(Governor.run_command(command))
    locations.append(Governor.lookup(ip))
print ", ".join(locations)
