#!/bin/bash


# ps -aux | grep python


echo Script name: $0
echo $1 arguments



# Kill all running processes
pkill -f "KronOS_Screen.py"
pkill -f "KronOS_Radio.py"
pkill -f "KronOS_Clock.py"


if [ $1 = "stop" ]; then
    echo "KronOS has been TERMIANTED!"
    exit
fi


filename=alarm.ini

echo "[ALARM]" > $filename
echo 'lin1 = "null"' >> $filename
echo 'lin2 = "null"' >> $filename

python KronOS_Clock.py & disown


filename=radio.ini
echo "[RADIO]" > $filename
echo 'playing = "null"' >> $filename

python KronOS_Radio.py & disown


python KronOS_Screen.py & disown
