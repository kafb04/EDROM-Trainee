import cv2
import numpy as np

def reconhecimento_cores(frame):
  hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

  azul_claro = np.array([90, 50, 50]) 
  
  azul_escuro = np.array([130, 255, 255])

  mask_azul = cv2.inRange(hsv, azul_claro, azul_escuro)

  vermelho = [0, 0, 255]

  frame[np.where(mask_azul> 0)] = vermelho

  return frame

camera = cv2.VideoCapture(0)

while True: 
  captura_sucesso, frame = camera.read()
  
  frame_processado = reconhecimento_cores(frame)

  cv2.imshow('Reconhecimento de Cor', frame_processado)

  if cv2.waitKey(1) == 27: 
    break

camera.release()
cv2.destroyAllWindows()
