import cv2

# Haarcascade faylini yuklang
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Videodan yoki web-kameradan tasvir oling
cap = cv2.VideoCapture(0)  # 0 - default kamera, agar boshqa video fayl bo'lsa, yo'lni kiriting

while True:
    # Kadrni o'qing
    ret, frame = cap.read()
    if not ret:
        break
    
    # Tasvirni kul rangga aylantiring
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Yuzlarni aniqlash
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Aniqlangan yuzlar atrofida to'rtburchak chizing
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    # Natijani ko'rsatish
    cv2.imshow('Yuzni aniqlash', frame)
    
    # 'q' tugmasi bosilganda dasturdan chiqish
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Resurslarni ozod qiling
cap.release()
cv2.destroyAllWindows()
