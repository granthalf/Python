import cv2

# 0 = première webcam MF
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

if not cap.isOpened():
    print("Impossible d'ouvrir la webcam via Media Foundation")
    exit()

print("Webcam ouverte via Media Foundation !")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Erreur de capture")
        break

    cv2.imshow("MF Webcam", frame)

    if cv2.waitKey(1) == 27:  # ESC pour quitter
        break

cap.release()
cv2.destroyAllWindows()
