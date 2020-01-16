import cv2
import json

w = 640
h = 360
frameNr = 379
# init all data as 1

animData = [[[ 0 for x in range(w)] for y in range(h)] for f in range(frameNr)]


for f in range(frameNr):
    fileName = "./vid_data/%03d.jpg" % f
    print(fileName)
    img = cv2.imread(fileName,0)
    for i in range(h):
        for j in range(w):
            if img[i][j] < 128:
                # print("has pixel " + str(i) + "," + str(j))
                animData[f][i][j] = 1 # give to animation data,0 means no pixel show

dataString = json.dumps(animData)
dataFile = open("animData.json", "w")

dataFile.write(dataString)

dataFile.close()



# demo
# img = cv2.imread("./vid_data/000.jpg",0)
# print(img[359][639])