import cv2
imagen_color = cv2.imread('mi.jpg')
if imagen_color is None:
    print("Error al cargar la imagen.")
    exit()

imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)
imagen_ecualizada = cv2.equalizeHist(imagen_gris)
# Guardar la imagen resultante
cv2.imwrite('imagen_ecualizada.jpg', imagen_ecualizada)
# Mostrar la imagen original y la imagen ecualizada
cv2.imshow('Imagen Original en Grises', imagen_gris)
cv2.imshow('Imagen Ecualizada', imagen_ecualizada)
cv2.waitKey(0)
cv2.destroyAllWindows()