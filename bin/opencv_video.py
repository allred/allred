#!/usr/bin/env python
# https://thedatafrog.com/en/articles/human-detection-video/
import cv2 as cv
import glob
import numpy as np
import os
import subprocess
import time

dir_caps = f"{os.environ['HOME']}/tmp/motion"
file_cap = "76-20210713163948.mkv"
dir_out = f"{os.environ['HOME']}/tmp/opencv"
file_out = f"{file_cap}.mp4"
path_ffmpeg = "/usr/local/bin/ffmpeg"
path_ffmpeg = "/home/linuxbrew/.linuxbrew/bin/ffmpeg"

#cmd_conv = f"{path_ffmpeg} -y -i {dir_caps}/{file_cap} -codec copy {dir_out}/{file_out}"
#subprocess.run(cmd_conv.split(" "))

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

def process_file(filepath):
    #cap = cv.VideoCapture(f"{dir_out}/{file_out}")
    cap = cv.VideoCapture(filepath)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            #print(f"cannot receive frame {ret} {frame}")
            break
        if frame is None:
            #print(f"cannot receive frame: ret:{ret} frame:{frame}")
            break 
        #assert type(frame) == "foo"
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        #cv.imshow("frame", gray)
        if cv.waitKey(1) == ord("q"):
            break
        #boxes, weights = hog.detectMultiScale(frame, winStride=(8,8))
        boxes, weights = hog.detectMultiScale(gray, winStride=(8,8))
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
        for (xA, yA, xB, yB) in boxes:
             cv.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        if (len(boxes) > 0 or len(weights) > 0 or mode == "debug"):
            print(boxes, weights)
            cv.imshow("frame", frame)
            input("Press Enter to continue...")
            time.sleep(.1)
    cap.release()
    cv.destroyAllWindows()

if __name__ == '__main__':
    print("hit 'q' to stop")
    mode = "debug"
    mode = "nodebug"
    files = [
        f"{dir_caps}/{file_cap}",
            ]
    files = glob.glob(f"{dir_caps}/*")
    for f in files:
        print(f"processing {f}")
        process_file(f)
