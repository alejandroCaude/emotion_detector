import cv2
from deepface import DeepFace

traduccion_emociones = {
    "angry": "Enfadado",
    "disgust": "Disgustado",
    "fear": "Miedo",
    "happy": "Feliz",
    "sad": "Triste",
    "surprise": "Sorprendido",
    "neutral": "Neutral"
}

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    try:
        resultado = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
        emocion = resultado[0]['dominant_emotion'] 
        emocion_es = traduccion_emociones.get(emocion, emocion) 
        
      
        detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        rostros = detector.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        for (x, y, w, h) in rostros:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, emocion_es, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    except Exception as e:
        print("Error detectando emoción:", e)

    cv2.imshow("Detección de Emociones", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
