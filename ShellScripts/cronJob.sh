read -p "Please input time interval(Second) which you want to execute this script: " sleepSecond
echo "sleep second $sleepSecond"
#sleepSecond=$[$sleepMinute]
echo "$sleepSecond"

while [ true ]
do
  sh monitorCpuUsage_v1.sh
  sleep $sleepSecond
  echo "$sleepSecond seconds past"
done
