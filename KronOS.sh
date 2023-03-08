#!/bin/bash


# ps -aux | grep python


#echo Script name: $0
#echo $1

#Exit vim Esc :wq

# Kill all running processes
pkill -f "KronOS_Screen.py"
pkill -f "KronOS_Radio.py"
pkill -f "KronOS_Clock.py"
pkill -f "KronOS_UI.py"
pkill -f "KronOS_Gif.py"


if [ "$1" = "stop" ]; then
    echo "KronOS has been TERMIANTED!"
    exit
fi

if [ "$1" = "reboot" ]; then
    echo "Rebooting"
    $KronOS $0 && exit
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


python KronOS_Gif.py & disown


python ./KronOS_UI.py
