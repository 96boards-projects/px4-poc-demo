from __future__ import print_function
from dronekit import connect, VehicleMode
import time
import os

vehicle = connect("/dev/ttyACM0", wait_ready=False, baud=57600)
fw_ver = str(vehicle.version)

os.system("ffmpeg -f v4l2 -video_size 1920x1080 -i /dev/video2 -vf 'drawtext=textfile=/tmp/test_overlay.txt:reload=1:x=0:y=0:fontsize=24:fontcolor=white'  -map 0 -c:v libx264 -f tee 'output.mp4|[f=nut]pipe:' | ffplay -an pipe: &")

while True:
    text_file = open("/tmp/test_overlay.txt", "w")
    buf = "Firmware: " + fw_ver + '\n' + "Status: " + str(vehicle.system_status.state) + "\nHeading: " + str(vehicle.heading) + "\nGPS Status: " + str(vehicle.gps_0)
    text_file.write(buf)
    text_file.close()
    time.sleep(1)


