import cv2
from cvzone.HandTrackingModule import HandDetector

webcam = cv2.VideoCapture(0)
rastrador = HandDetector(detectionCon=0.8, maxHands = 2)

while True:
    sucesso,imagem = webcam.read()
    coordenadas,imagem_maos = rastrador.findHands(imagem)
    print(coordenadas)

    cv2.imshow("Projeto 4 - IA",imagem)

    if cv2.waitKey(1) != -1:
        break

webcam.release()
cv2.destroyAllWindows()
