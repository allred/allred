#!/usr/bin/env python
import cv2 as cv
import numpy as np
import os
import subprocess

dir_caps = f"{os.environ['HOME']}/tmp/motion"
file_cap = "76-20210713163948.mkv"
dir_out = f"{os.environ['HOME']}/tmp/opencv"
file_out = f"{file_cap}.mp4"
path_ffmpeg = "/usr/local/bin/ffmpeg"

cmd_conv = f"{path_ffmpeg} -y -i {dir_caps}/{file_cap} -codec copy {dir_out}/{file_out}"
subprocess.run(cmd_conv.split(" "))

cap = cv.VideoCapture(f"{dir_out}/{file_out}")
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print(f"cannot receive frame {ret}")
        #break
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow("frame", gray)
    if cv.waitKey(1) == ord("q"):
        break
    

cap.release()
cv.destroyAllWindows()
