import cv2
import time

Conf_threshold = 0.7
NMS_threshold = 0.7

COLORS = [(0, 255, 0), (0, 0, 255), (255, 0, 0), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class_name = []
with open('coco.txt', 'r') as f:
    class_name = [cname.strip() for cname in f.readlines()]


camera = cv2.VideoCapture(0)

net = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg', 'darknet')

model = cv2.dnn_DetectionModel(net)

model.setInputParams(size=(416, 416), scale=1/255, swapRB=True)


frame_counter = 0

start = time.time()

while True:

    ret, frame = camera.read()
    
    frame_counter += 1

    classes, scores, boxes = model.detect(frame, Conf_threshold, NMS_threshold)

    end = time.time() - start

    for (classid, score, box) in zip(classes, scores, boxes):
        if 0 <= classid < len(class_name):
            color = COLORS[int(classid) % len(COLORS)]
            label = "%s : %f" % (class_name[classid], score)
            cv2.rectangle(frame, box, color, 1)
            cv2.putText(frame, label, (box[0], box[1]-10), cv2.FONT_HERSHEY_COMPLEX, 0.3, color, 1)

    fps = frame_counter/end

    cv2.putText(frame, f'FPS: {fps}', (20, 50), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow('Deteccao de Objetos', frame)

    if cv2.waitKey(1) == 27:
        break
    
camera.release()
cv2.destroyAllWindows()
