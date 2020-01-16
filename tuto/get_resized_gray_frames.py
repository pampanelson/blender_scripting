import cv2
vidcap = cv2.VideoCapture('vid1280x720.mp4')
success,image = vidcap.read()
count = 0
blackThresh = 5

while success:
    success,image = vidcap.read()
    resize = cv2.resize(image, (640, 360)) 
    gray = cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

    for i in range(360):
        for j in range(640):
            if gray[i][j] > blackThresh:
                gray[i][j] = 255

    cv2.imwrite("./vid_data/%03d.jpg" % count, gray)     
    if cv2.waitKey(10) == 27:                     
        break
    count += 1