import cv2
# Cargar la imagen 
imagen_color = cv2.imread('monedas.png')
# Convertir  a escala de grises
imagen_gris = cv2.cvtColor(imagen_color, cv2.COLOR_BGR2GRAY)
# Mostrar la imagen 
cv2.imshow('Imagen en escala de grises', imagen_gris)
# Guardar la imagen en escala de grises
cv2.imwrite('IMAGEN_A_ESCALAs.jpg', imagen_gris)
cv2.waitKey(0)
cv2.destroyAllWindows()

