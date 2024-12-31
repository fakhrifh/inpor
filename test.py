import cv2

# Buka kamera (indeks 0 adalah kamera pertama)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak dapat membuka kamera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Tidak dapat membaca frame")
        break

    # Tampilkan frame di jendela
    cv2.imshow("Kamera", frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
