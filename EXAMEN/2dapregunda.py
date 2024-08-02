import cv2
# Cargar la imagen 
imagen = cv2.imread('mi.jpg')
# Convertir a escala de grises
imagen_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
bordes = cv2.Canny(imagen_gris, 100, 200)
# Mostrar la imagen con los bordes detectados
cv2.imshow('Bordes detectados', bordes)
# Guardar la imagen con los bordes detectados
cv2.imwrite('BORDES.jpg', bordes)
cv2.waitKey(0)
cv2.destroyAllWindows()
