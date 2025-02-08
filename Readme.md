# Reconocimiento Facial y Emociones en Python

Este proyecto utiliza OpenCV y DeepFace para realizar el **reconocimiento facial** y detectar **emociones** en tiempo real desde la cámara web. El programa procesa cada fotograma capturado por la cámara, detecta las caras en la imagen y muestra un cuadro alrededor, además de identificar y mostrar la emoción dominante en cada cara.

## ¿Qué hace?

- **Detección de rostro**: Utiliza OpenCV para detectar caras en tiempo real a través de la cámara web.
- **Análisis de emociones**: Utiliza DeepFace para analizar las emociones de las personas en las caras detectados.
- **Traducción de emociones**: Las emociones detectadas son mostradas en español, basándose en una lista predefinida de emociones.
- **Visualización**: Las caras detectadas se marcan con un cuadro verde y la emoción detectada se escribe encima de la cara en la imagen.

### Emociones soportadas:

- **angry**: Enfadado
- **disgust**: Disgustado
- **fear**: Miedo
- **happy**: Feliz
- **sad**: Triste
- **surprise**: Sorprendido
- **neutral**: Neutral

El programa muestra una ventana con la cámara, donde cada cara detectada se marca con un cuadro y la emoción correspondiente. El video continuará hasta que el usuario presione la tecla 'q' para salir.

## Notas

- El programa utiliza un detector de caras basado en Haar cascades de OpenCV.
- La emoción se detecta mediante el modelo preentrenado de DeepFace, que analiza la imagen para identificar la emoción dominante.
