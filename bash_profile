if [ -f ~/.bashrc ]; then
  . ~/.bashrc
fi
let upSeconds="$(/usr/bin/cut -d. -f1 /proc/uptime)"
let secs=$((${upSeconds}%60))
let mins=$((${upSeconds}/60%60))
let hours=$((${upSeconds}/3600%24))
let days=$((${upSeconds}/86400))
UPTIME=`printf "%d days, %02dh%02dm%02ds" "$days" "$hours" "$mins" "$secs"`

ATTEMPTS=`grep -w 'sshd.*Invalid' -c /var/log/auth.log`

LOGINLOCATION=`python /home/pi/scripts/ip_lookup.py`

cpuTemp0=$(cat /sys/class/thermal/thermal_zone0/temp)
cpuTemp1=$(($cpuTemp0/1000))
cpuTemp2=$(($cpuTemp0/100))
cpuTempM=$(($cpuTemp2 % $cpuTemp1))

gpuTemp=$(/opt/vc/bin/vcgencmd measure_temp)
gpuTemp=${gpuTemp//\'/º}
GPUTEMP=${gpuTemp//temp=/}

lastLogin=$(cat /var/log/auth.log | grep 'sshd.*Accepted' | tail -1)

echo "    Uptime..................: ${UPTIME}"
echo "    Last login location.....: ${LOGINLOCATION}"
echo "    Invalid login attempts..: ${ATTEMPTS}"
echo "    CPU temp................: $cpuTemp1.$cpuTempMºC"
echo "    GPU temp................: ${GPUTEMP}"
