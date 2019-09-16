import os
import cv2
import numpy as np
from upload_data import upload_file


def process_frame(file, bucket, working_dir):
    cap = cv2.VideoCapture(file)
    f = open(file.split('.mov')[0] + '.face')
    break_the_loop = False
    count = 0
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        read_line = f.readline()
        print(read_line)
        if read_line == '':
            break_the_loop = True
        else:
            # print(read_line)
            try:
                x, y, w, h = map(int, read_line.strip().split(' '))
            except:
                print('exception')
                pass
            print('x= ' + str(x) + ' y= ' + str(y) + ' w= ' + str(w) + ' h= ' + str(h))
            roi = frame[y:h, x:w]
            file_name = file.split('.mov')[0] + str(count) + '.jpg'
            cv2.imwrite(file.split('.mov')[0] + str(count) + '.jpg', roi)
            object_name = str(working_dir) + str(file_name)
            upload_file(file_name, bucket, object_name)
            # cv2.imwrite()
            os.remove(file_name)
            count += 1
        if cv2.waitKey(1) & 0xFF == ord('q') or break_the_loop:
            break

    return


def process_dataset(path, bucket, working_dir):
    for root, dir, filenames in os.walk(path):
        for file in filenames:
            if file.endswith('.mov'):
                file_path = os.path.join(root, file)
                process_frame(file_path, bucket, working_dir)
